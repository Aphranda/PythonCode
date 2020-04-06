import json
from urllib.parse import urlparse
from uuid import uuid4
import hashlib
from time import time
import requests
from flask import Flask, jsonify, request
from argparse import ArgumentParser


class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.nodes = set()
        self.new_block(proof=100, previous_hash=1)

    def register_node(self, address: str):
        #http://127.0.0.1:5001
        """注册节点"""
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)

    def valid_chain(self, chain) -> bool:
        last_block = chain[0]
        current_index = 1

        while current_index < len(chain):
            block = chain[current_index]

            if block['previous_hash'] != self.hash(last_block):
                return False
            if not self.valid_proof(last_block['proof'], block['proof']):
                return False
            last_block = block
            current_index += 1

        return True

    def resolve_conflicts(self) -> bool:
        neighbours = self.nodes

        max_length = len(self.chain)
        new_chain = None

        for node in neighbours:
            response = requests.get(f'http://{node}/chain')
            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']
                if length > max_length and self.valid_chain(chain):
                    max_length = length
                    new_chain = chain

        if new_chain:
            self.chain = new_chain
            return True
        return False

    def new_block(self, proof, previous_hash=None):
        """add new block"""
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.last_block)
        }
        self. current_transactions = []
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """add new transaction"""
        # 封装交易记录放置于列表中
        self.current_transactions.append(
            {
                'sender': sender,
                'recipient': recipient,
                'amount': amount
            }
        )
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        """calculate hash"""
        block_string = json.dumps(block, sort_keys=True).encode()
        hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]

    def proof_of_work(self, last_proof: int) -> int:
        """工作量证明循环验证"""
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        # print(proof)
        return proof

    def valid_proof(self, last_proof: int, proof: int) -> bool:
        """工作量证明循环验证"""
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()

        if guess_hash[0:4] == "0000":
            print(guess_hash)
            return True
        else:
            return False


app = Flask(__name__)  # Flask 生成小型服务器
blockchain = Blockchain()  # 区块链类实例化

node_indentifier = str(uuid4()).replace('-', '')


@app.route('/transaction/new', methods=['POST'])
def new_transaction():
    """路由：添加新交易"""
    values = request.get_json()
    required = ["sender", "recipient", 'amount']
    if values is None:
        return "Messing values", 400
    if not all(k in values for k in required):
        return "Missing values", 400

    index = blockchain.new_transaction(values['sender'],
                                       values['recipient'],
                                       values['amount'])

    response = {"message": f'Transcation will be added to Block {index}'}
    return jsonify(response), 201


@app.route('/mine', methods=['GET'])
def mine():
    """路由：挖矿"""
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    blockchain.new_transaction(sender="0",
                               recipient=node_indentifier,
                               amount=1)
    block = blockchain.new_block(proof, None)

    response = {
        'message': "New Block Forged",
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash']
    }

    return jsonify(response), 200


@app.route('/chain', methods=['GET'])
def full_chain():
    """路由：区块链信息"""
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return jsonify(response), 200  # Flask里将json变成字符串


@app.route('/nodes/register', methods=['POST'])
def register_nodes():
    """路由：注册节点"""
    values = request.get_json()

    nodes = values.get('nodes')
    if nodes is None:
        return "Error: please supply a valid list of nodes", 400
    for node in nodes:
        blockchain.register_node(node)

    response = {
        "message": "New nodes have been added",
        "total_nodes": list(blockchain.nodes)
    }
    return jsonify(response), 201


@app.route('/nodes/resolve', methods=['GET'])
def consensus():
    replaced = blockchain.resolve_conflicts()

    if replaced:
        response = {
            'Message': 'Our chain was replaced',
            'new chain': blockchain.chain
        }
    else:
        response = {
            'Message': 'Our chain is authoritative',
            'chain': blockchain.chain
        }
    return jsonify(response), 200


if __name__ == '__main__':
    parse = ArgumentParser()
    parse.add_argument('-p', '--port', default=5001, type=int, help='port to listen to')
    args = parse.parse_args()
    port = args.port
    app.run(host='0.0.0.0', port=port)