

# # line_edit = [
# #     "self.lineEdit_Temp", "self.lineEdit_VCC", "self.lineEdit_Bias", "self.lineEdit_TxP", "self.lineEdit_RxP", "self.lineEdit_OLT", "self.lineEdit_OTC"
# # ]

# # line_threshold = [
# #     ['Temp High Alarm', 'Temp Low Alarm', 'Temp High Warning', 'Temp Low Warning'],
# #     ['Voltage High Alarm', 'Voltage Low Alarm', 'Voltage High Warning', 'Voltage Low Warning'],
# #     ['Bias High Alarm', 'Bias Low Alarm', 'Bias High Warning', 'Bias Low Warning'],
# #     ['TX Power High Alarm', 'TX Power Low Alarm', 'TX Power High Warning', 'TX Power Low Warning'],
# #     ['RX Power High Alarm', 'RX Power Low Alarm', 'RX Power High Warning', 'RX Power Low Warning'],
# #     ['Optional Laser Temp High Alarm', 'Optional Laser Temp Low Alarm', 'Optional Laser Temp High Warning', 'Optional Laser Temp Low Warning'],
# #     ['Optional TEC Current High Alarm', 'Optional TEC Current Low Alarm', 'Optional TEC Current High Warning', 'Optional TEC Current Low Warning']
# # ]
# # line_color = [
# #     "background-color:green", "background-color:red"
# # ]
# # line_data = [
# #     'Temperature', "Vcc", 'Bias', 'TX Power', 'RX Power', 'OLT', 'OTC'
# # ]


# # dict_data = {
# #     'Temp High Alarm': 95.0, 'Temp Low Alarm': -78.0, 'Temp High Warning': 85.0, 'Temp Low Warning': -118.0,
# #     'Voltage High Alarm': 3.6147, 'Voltage Low Alarm': 2.923, 'Voltage High Warning': 3.4845, 'Voltage Low Warning': 3.0266,
# #     'Bias High Alarm': 14.948, 'Bias Low Alarm': 1.582, 'Bias High Warning': 11.804, 'Bias Low Warning': 2.678,
# #     'TX Power High Alarm': 3.0042155738307215, 'TX Power Low Alarm': -10.048037084028206, 'TX Power High Warning': 2.4978517583225104, 'TX Power Low Warning': -8.642314854321778,
# #     'RX Power High Alarm': 3.0042155738307215, 'RX Power Low Alarm': -17.772835288524167, 'RX Power High Warning': 2.4978517583225104, 'RX Power Low Warning': -13.279021420642824,
# #     'Optional Laser Temp High Alarm': 0.0, 'Optional Laser Temp Low Alarm': 0.0, 'Optional Laser Temp High Warning': 0.0, 'Optional Laser Temp Low Warning': 0.0,
# #     'Optional TEC Current High Alarm': 0.0, 'Optional TEC Current Low Alarm': 0.0, 'Optional TEC Current High Warning': 0.0, 'Optional TEC Current Low Warning': 0.0,
# #     'Temperature': 14.0546875, 'Vcc': 3.2318, 'Bias': 6.392, 'TX Power': -0.42057664554595453, 'RX Power': -18.927900303521316, 'OLT': 0.0, 'OTC': 0.0
# # }


# # def classify(key, value, data, line, color):
# #     box = []
# #     boxes = []
# #     item = {}
# #     for i, n  in enumerate(key):
# #         for j in value[i]:
# #             if data[n] > data[j]:
# #                 box.append(1)
# #             elif data[n] < data[j]:
# #                 box.append(0)
# #             else:
# #                 box.append(2)
# #     for k in range(len(box)//4):
# #         boxes.append(box[4*k:4*k+4])
# #     print(boxes)
# #     for m in boxes[0:-2]:
# #         for n in range(2):
# #             if m[2*n] == 0:
# #                 m[2*n] = color[0]
# #             else:
# #                 m[2*n] = color[1]
# #             if m[3**n] == 1:
# #                 m[3**n] = color[0]
# #             else:
# #                 m[3**n] = color[1]
# #     for m in boxes[-2:]:
# #         for n in range(2):
# #             if m[2*n] == 0:
# #                 m[2*n] = color[0]
# #             elif m[2*n] == 2:
# #                 m[2*n] = color[0]
# #             else:
# #                 m[2*n] = color[1]
# #             if m[3**n] == 1:
# #                 m[3**n] = color[0]
# #             elif m[3**n] == 2:
# #                 m[3**n] = color[0]
# #             else:
# #                 m[3**n] = color[1]
# #     for i, n in enumerate(boxes):
# #         for p in range(1,5):
# #             item[line[i] + "_" + str(p)] = n[p-1]
# #     print(item)
# #     for i in item:
# #         print(i, item[i])







# # classify(line_data, line_threshold, dict_data, line_edit, line_color)

# # aw_thresholds = [
# #     ['Temp High Alarm', 'Temp Low Alarm', 'Temp High Warning', 'Temp Low Warning'],
# #     ['Voltage High Alarm', 'Voltage Low Alarm', 'Voltage High Warning', 'Voltage Low Warning'],
# #     ['Bias High Alarm', 'Bias Low Alarm', 'Bias High Warning', 'Bias Low Warning'],
# #     ['TX Power High Alarm', 'TX Power Low Alarm', 'TX Power High Warning', 'TX Power Low Warning'],
# #     ['RX Power High Alarm', 'RX Power Low Alarm', 'RX Power High Warning', 'RX Power Low Warning']
# #     ]

# # key_words = []


# line_edit = [
#     'self.lineEdit_Temp_Q_1', 'self.lineEdit_Temp_Q_2', 'self.lineEdit_Temp_Q_3', 'self.lineEdit_Temp_Q_4', 
#     'self.lineEdit_VCC_Q_1', 'self.lineEdit_VCC_Q_2', 'self.lineEdit_VCC_Q_3', 'self.lineEdit_VCC_Q_4',
#     'self.lineEdit_Bias_Q_CH1_1', 'self.lineEdit_Bias_Q_CH1_2', 'self.lineEdit_Bias_Q_CH1_3', 'self.lineEdit_Bias_Q_CH1_4', 
#     'self.lineEdit_Bias_Q_CH2_1', 'self.lineEdit_Bias_Q_CH2_2', 'self.lineEdit_Bias_Q_CH2_3', 'self.lineEdit_Bias_Q_CH2_4', 
#     'self.lineEdit_Bias_Q_CH3_1', 'self.lineEdit_Bias_Q_CH3_2', 'self.lineEdit_Bias_Q_CH3_3', 'self.lineEdit_Bias_Q_CH3_4', 
#     'self.lineEdit_Bias_Q_CH4_1', 'self.lineEdit_Bias_Q_CH4_2', 'self.lineEdit_Bias_Q_CH4_3', 'self.lineEdit_Bias_Q_CH4_4',
#     'self.lineEdit_TXP_Q_CH1_1', 'self.lineEdit_TXP_Q_CH1_2', 'self.lineEdit_TXP_Q_CH1_3', 'self.lineEdit_TXP_Q_CH1_4', 
#     'self.lineEdit_TXP_Q_CH2_1', 'self.lineEdit_TXP_Q_CH2_2', 'self.lineEdit_TXP_Q_CH2_3', 'self.lineEdit_TXP_Q_CH2_4', 
#     'self.lineEdit_TXP_Q_CH3_1', 'self.lineEdit_TXP_Q_CH3_2', 'self.lineEdit_TXP_Q_CH3_3', 'self.lineEdit_TXP_Q_CH3_4', 
#     'self.lineEdit_TXP_Q_CH4_1', 'self.lineEdit_TXP_Q_CH4_2', 'self.lineEdit_TXP_Q_CH4_3', 'self.lineEdit_TXP_Q_CH4_4',
#     'self.lineEdit_RXP_Q_CH1_1', 'self.lineEdit_RXP_Q_CH1_2', 'self.lineEdit_RXP_Q_CH1_3', 'self.lineEdit_RXP_Q_CH1_4', 
#     'self.lineEdit_RXP_Q_CH2_1', 'self.lineEdit_RXP_Q_CH2_2', 'self.lineEdit_RXP_Q_CH2_3', 'self.lineEdit_RXP_Q_CH2_4', 
#     'self.lineEdit_RXP_Q_CH3_1', 'self.lineEdit_RXP_Q_CH3_2', 'self.lineEdit_RXP_Q_CH3_3', 'self.lineEdit_RXP_Q_CH3_4', 
#     'self.lineEdit_RXP_Q_CH4_1', 'self.lineEdit_RXP_Q_CH4_2', 'self.lineEdit_RXP_Q_CH4_3', 'self.lineEdit_RXP_Q_CH4_4'
#     ]
# line_color = [
#     "background-color:green", "background-color:red"
# ]
# line_data = [
#     ['Temperature'], 
#     ['Vcc'], 
#     ['TX1 Bias', 'TX2 Bias', 'TX3 Bias', 'TX4 Bias'], 
#     ['TX1 Power', 'TX2 Power', 'TX3 Power', 'TX4 Power'], 
#     ['RX1 Power', 'RX2 Power', 'RX3 Power', 'RX4 Power'], 
# ]
# line_threshold = [
#     ['Temp High Alarm', 'Temp Low Alarm', 'Temp High Warning' , 'Temp Low Warning'],
#     ['Voltage High Alarm', 'Voltage Low Alarm', 'Voltage High Warning', 'Voltage Low Warning'],
#     ['Bias High Alarm' , 'Bias Low Alarm' , 'Bias High Warning' , 'Bias Low Warning'],
#     ['RX Power High Alarm' , 'RX Power Low Alarm', 'RX Power High Warning' , 'RX Power Low Warning'],
#     ['TX Power High Alarm', 'TX Power Low Alarm', 'TX Power High Warning', 'TX Power Low Warning']
# ]
# dict_data = {
#     'Temperature': 33.0, 

#     'Vcc': 2.7959, 

#     'TX1 Bias': 7.152, 
#     'TX2 Bias': 7.088, 
#     'TX3 Bias': 7.056, 
#     'TX4 Bias': 6.672, 

#     'TX1 Power': 0.21437396467089756, 
#     'TX2 Power': 0.28977705208778, 
#     'TX3 Power': 0.24485667699166974, 
#     'TX4 Power': 0.21189299069938092, 
    
#     'RX1 Power': -18.927900303521316, 
#     'RX2 Power': -18.927900303521316, 
#     'RX3 Power': -18.927900303521316, 
#     'RX4 Power': -18.927900303521316, 
    
#     'Temp High Alarm': 85.0, 
#     'Temp Low Alarm': -118.0, 
#     'Temp High Warning': 70.0, 
#     'Temp Low Warning': 0.0, 
    
#     'Voltage High Alarm': 3.5845, 
#     'Voltage Low Alarm': 2.8946, 
#     'Voltage High Warning': 3.4845, 
#     'Voltage Low Warning': 3.1, 
    
#     'RX Power High Alarm': 4.0373805036385555, 
#     'RX Power Low Alarm': -19.1721462968355, 
#     'RX Power High Warning': 2.361088015872817, 
#     'RX Power Low Warning': -15.00312917381596, 
    
#     'Bias High Alarm': 14.948, 
#     'Bias Low Alarm': 0.0, 
#     'Bias High Warning': 11.804, 
#     'Bias Low Warning': 1.582, 
    
#     'TX Power High Alarm': 4.0373805036385555, 
#     'TX Power Low Alarm': -10.00869458712629, 
#     'TX Power High Warning': 2.361088015872817, 
#     'TX Power Low Warning': -7.907531512466263
#     }

# def classify_qsfp(key, value, data, line, color):
#     box = {}
#     boxes = []
#     item = []
#     items = {}
#     for i in range(5):
#         for j in range(4):
#             box[value[i][j]] = key[i]
#     for m in box:
#         for n in box[m]:
#             if data[n] > data[m]:
#                 boxes.append(0)
#             else:
#                 boxes.append(1)
#     for i in range(1,5):
#         if boxes[0:8][2*i-2] == 1:
#             item.append(color[0])
#         else:
#             item.append(color[1])
#         if boxes[0:8][2*i-1] == 0:
#             item.append(color[0])
#         else:
#             item.append(color[1])
#     for j in range(0,11,2):
#         for s in boxes[8:56][4*j:4*j+4]:

#             if s == 0:
#                 item.append(color[1])
#             else:
#                 item.append(color[0])
#     for k in range(1,13,2):
#         for s in boxes[8:56][4*k:4*k+4]:
#             if s == 1:
#                 item.append(color[1])
#             else:
#                 item.append(color[0])
#     for i, n in enumerate(item):
#         items[line[i]] = n
#     return items
         
# classify_qsfp(line_data, line_threshold, dict_data, line_edit, line_color)
# b = []
# for i in range(1,5):
#     for j in range(1,5):
#         a = f'self.lineEdit_RXP_Q_CH{j}_{i}'
#         b.append(a)
#     print(b)

