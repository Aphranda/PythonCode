

# line_edit = [
#     "self.lineEdit_Temp", "self.lineEdit_VCC", "self.lineEdit_Bias", "self.lineEdit_TxP", "self.lineEdit_RxP", "self.lineEdit_OLT", "self.lineEdit_OTC"
# ]

# line_threshold = [
#     ['Temp High Alarm', 'Temp Low Alarm', 'Temp High Warning', 'Temp Low Warning'],
#     ['Voltage High Alarm', 'Voltage Low Alarm', 'Voltage High Warning', 'Voltage Low Warning'],
#     ['Bias High Alarm', 'Bias Low Alarm', 'Bias High Warning', 'Bias Low Warning'],
#     ['TX Power High Alarm', 'TX Power Low Alarm', 'TX Power High Warning', 'TX Power Low Warning'],
#     ['RX Power High Alarm', 'RX Power Low Alarm', 'RX Power High Warning', 'RX Power Low Warning'],
#     ['Optional Laser Temp High Alarm', 'Optional Laser Temp Low Alarm', 'Optional Laser Temp High Warning', 'Optional Laser Temp Low Warning'],
#     ['Optional TEC Current High Alarm', 'Optional TEC Current Low Alarm', 'Optional TEC Current High Warning', 'Optional TEC Current Low Warning']
# ]
# line_color = [
#     "background-color:green", "background-color:red"
# ]
# line_data = [
#     'Temperature', "Vcc", 'Bias', 'TX Power', 'RX Power', 'OLT', 'OTC'
# ]


# dict_data = {
#     'Temp High Alarm': 95.0, 'Temp Low Alarm': -78.0, 'Temp High Warning': 85.0, 'Temp Low Warning': -118.0,
#     'Voltage High Alarm': 3.6147, 'Voltage Low Alarm': 2.923, 'Voltage High Warning': 3.4845, 'Voltage Low Warning': 3.0266,
#     'Bias High Alarm': 14.948, 'Bias Low Alarm': 1.582, 'Bias High Warning': 11.804, 'Bias Low Warning': 2.678,
#     'TX Power High Alarm': 3.0042155738307215, 'TX Power Low Alarm': -10.048037084028206, 'TX Power High Warning': 2.4978517583225104, 'TX Power Low Warning': -8.642314854321778,
#     'RX Power High Alarm': 3.0042155738307215, 'RX Power Low Alarm': -17.772835288524167, 'RX Power High Warning': 2.4978517583225104, 'RX Power Low Warning': -13.279021420642824,
#     'Optional Laser Temp High Alarm': 0.0, 'Optional Laser Temp Low Alarm': 0.0, 'Optional Laser Temp High Warning': 0.0, 'Optional Laser Temp Low Warning': 0.0,
#     'Optional TEC Current High Alarm': 0.0, 'Optional TEC Current Low Alarm': 0.0, 'Optional TEC Current High Warning': 0.0, 'Optional TEC Current Low Warning': 0.0,
#     'Temperature': 14.0546875, 'Vcc': 3.2318, 'Bias': 6.392, 'TX Power': -0.42057664554595453, 'RX Power': -18.927900303521316, 'OLT': 0.0, 'OTC': 0.0
# }


# def classify(key, value, data, line, color):
#     box = []
#     boxes = []
#     item = {}
#     for i, n  in enumerate(key):
#         for j in value[i]:
#             if data[n] > data[j]:
#                 box.append(1)
#             elif data[n] < data[j]:
#                 box.append(0)
#             else:
#                 box.append(2)
#     for k in range(len(box)//4):
#         boxes.append(box[4*k:4*k+4])
#     print(boxes)
#     for m in boxes[0:-2]:
#         for n in range(2):
#             if m[2*n] == 0:
#                 m[2*n] = color[0]
#             else:
#                 m[2*n] = color[1]
#             if m[3**n] == 1:
#                 m[3**n] = color[0]
#             else:
#                 m[3**n] = color[1]
#     for m in boxes[-2:]:
#         for n in range(2):
#             if m[2*n] == 0:
#                 m[2*n] = color[0]
#             elif m[2*n] == 2:
#                 m[2*n] = color[0]
#             else:
#                 m[2*n] = color[1]
#             if m[3**n] == 1:
#                 m[3**n] = color[0]
#             elif m[3**n] == 2:
#                 m[3**n] = color[0]
#             else:
#                 m[3**n] = color[1]
#     for i, n in enumerate(boxes):
#         for p in range(1,5):
#             item[line[i] + "_" + str(p)] = n[p-1]
#     print(item)
#     for i in item:
#         print(i, item[i])







# classify(line_data, line_threshold, dict_data, line_edit, line_color)

trans_data = [0x7e, 0x10, 0x80, 0x03, 0x00, 0x00, 0x00, 0x7e]
trans_len = sum(trans_data[1:-2])
print(hex(trans_len))