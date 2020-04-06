Imports System
Imports System.IO.Ports

Public Class UARTTOIIC


    '字段
    Private _uartComStr As String
    '属性
    Property uartComStr() As String
        Get
            Return _uartComStr
        End Get
        Set(ByVal value As String)
            _uartComStr = value
        End Set
    End Property

    Public WithEvents _CommunSerialPort As SerialPort
    '方法
    Function IICPortClose() As Boolean
        Try

            _CommunSerialPort.Close()
        Catch
            MessageBox.Show("设备断开失败")
            Return False
        End Try
        Return True

    End Function
    '方法
    Function IICPortOpen() As Boolean
        Try
            _CommunSerialPort = New IO.Ports.SerialPort(_uartComStr, 57600, Parity.None, 8, StopBits.One)
            _CommunSerialPort.Open()
        Catch
            MessageBox.Show("通讯板COM口选择错误", "错误提示")
            Return False
        End Try
        Return True
    End Function



    'IIC 读
    'bIICNumber表示通讯板的IIC号码
    'bIICDeviceAddress表示通讯板IIC链接的模块的IIC地址
    'bIICDataStartAddress表示IIC通讯时读取的数据起始地址
    'bIICReadDataLength表示IIC通讯时读取数据的长度
    'aubUARTDrvReadBuf表示IIC读取的数据缓存
    '返回值0表示通讯失败，1表示通讯成功，2表示通讯结果异常，但是串口未断开链接
    Public Function STM32UartToIICSetSpeed(ByVal IICSpeed As Integer) As String

        Dim aubUARTWriteBuf_100(0 To 5) As Byte
        Dim aubUARTWriteBuf_200(0 To 5) As Byte
        Dim aubUARTWriteBuf_400(0 To 5) As Byte


        aubUARTWriteBuf_100(0) = Asc("#")                      'Start Byte
        aubUARTWriteBuf_100(1) = 6                             'Total Length
        aubUARTWriteBuf_100(2) = &H81
        aubUARTWriteBuf_100(3) = &H0
        aubUARTWriteBuf_100(4) = &H93
        aubUARTWriteBuf_100(5) = Asc("$")                       'Stop Byte

        aubUARTWriteBuf_200(0) = Asc("#")                      'Start Byte
        aubUARTWriteBuf_200(1) = 6                             'Total Length
        aubUARTWriteBuf_200(2) = &H81
        aubUARTWriteBuf_200(3) = &H0
        aubUARTWriteBuf_200(4) = &HEC
        aubUARTWriteBuf_200(5) = Asc("$")                       'Stop Byte

        aubUARTWriteBuf_400(0) = Asc("#")                      'Start Byte
        aubUARTWriteBuf_400(1) = 6                             'Total Length
        aubUARTWriteBuf_400(2) = &H81
        aubUARTWriteBuf_400(3) = &H1
        aubUARTWriteBuf_400(4) = &HA1
        aubUARTWriteBuf_400(5) = Asc("$")                       'Stop Byte

        Dim aubUARTReadBuf(0 To 3) As Byte
        Dim ausUARTRegReadCnt As Integer

        If IICSpeed = 100 Then
            Try
                _CommunSerialPort.Write(aubUARTWriteBuf_100, 0, 6)
            Catch
                Return "串口链接断开"
            End Try
        ElseIf IICSpeed = 200 Then
            Try
                _CommunSerialPort.Write(aubUARTWriteBuf_200, 0, 6)
            Catch
                Return "串口链接断开"
            End Try
        ElseIf IICSpeed = 400 Then
            Try
                _CommunSerialPort.Write(aubUARTWriteBuf_400, 0, 6)
            Catch
                Return "串口链接断开"
            End Try
        Else
            Try
                _CommunSerialPort.Write(aubUARTWriteBuf_100, 0, 6)
            Catch
                Return "串口链接断开"
            End Try
        End If

        Dim sleepdaley As Integer
        System.Threading.Thread.Sleep(10)
        While _CommunSerialPort.BytesToRead < 4
            If sleepdaley > 10 Then
                sleepdaley = 0
                ausUARTRegReadCnt = _CommunSerialPort.BytesToRead
                _CommunSerialPort.Read(aubUARTReadBuf, 0, ausUARTRegReadCnt)  '读取缓冲数据
                Return "串口链接断开"
            End If
            System.Threading.Thread.Sleep(2)
            sleepdaley = sleepdaley + 1
        End While

        ausUARTRegReadCnt = _CommunSerialPort.BytesToRead
        _CommunSerialPort.Read(aubUARTReadBuf, 0, ausUARTRegReadCnt)  '读取缓冲数据

        If (aubUARTReadBuf(0) = 35) And (aubUARTReadBuf(ausUARTRegReadCnt - 1) = 36) Then

            If IICSpeed = 100 Then
                If (aubUARTReadBuf(1) = 0) And (aubUARTReadBuf(2) = &H93) Then
                    Return "OK"
                End If
            ElseIf IICSpeed = 200 Then
                If (aubUARTReadBuf(1) = 0) And (aubUARTReadBuf(2) = &HEC) Then
                    Return "OK"
                End If
            ElseIf IICSpeed = 400 Then
                If (aubUARTReadBuf(1) = 1) And (aubUARTReadBuf(2) = &HA1) Then
                    Return "OK"
                End If
            Else
                If (aubUARTReadBuf(1) = 0) And (aubUARTReadBuf(2) = &H93) Then
                    Return "OK"
                End If
            End If
        Else
            Return "串口链接断开"
        End If

        Return "串口链接断开"
    End Function




    'IIC 读
    'bIICNumber表示通讯板的IIC号码
    'bIICDeviceAddress表示通讯板IIC链接的模块的IIC地址
    'bIICDataStartAddress表示IIC通讯时读取的数据起始地址
    'bIICReadDataLength表示IIC通讯时读取数据的长度
    'aubUARTDrvReadBuf表示IIC读取的数据缓存
    '返回值0表示通讯失败，1表示通讯成功，2表示通讯结果异常，但是串口未断开链接
    Public Function STM32UartToIICReadBytes(ByVal bIICNumber As Byte, _
                                    ByVal bIICDeviceAddress As Byte, _
                                    ByVal bIICDataStartAddress As Byte, _
                                    ByVal bIICReadDataLength As Integer, _
                                    ByRef aubUARTDrvReadBuf() As Byte
                                    ) As String

        Dim aubUARTWriteBuf(0 To 7) As Byte
        Dim aubUARTReadBuf(0 To 255) As Byte
        Dim ausUARTRegReadCnt As Integer
        Dim siFlag As Integer

        If (bIICReadDataLength = 0) Then
            Return "数据长度为0"
        End If

        aubUARTWriteBuf(0) = Asc("#")                      'Start Byte
        aubUARTWriteBuf(1) = 8                             'Total Length
        aubUARTWriteBuf(2) = 10                            '0A 读
        aubUARTWriteBuf(3) = bIICNumber                    '扩展IIC编号
        aubUARTWriteBuf(4) = bIICDeviceAddress             'IIC器件地址
        aubUARTWriteBuf(5) = bIICDataStartAddress          '寄存器地址
        aubUARTWriteBuf(6) = bIICReadDataLength            '读取长度
        aubUARTWriteBuf(7) = Asc("$")                      'Stop Byte

        Try
            _CommunSerialPort.Write(aubUARTWriteBuf, 0, 8)
        Catch
            Return "串口链接断开"
        End Try

        Dim sleepdaley As Integer

        While _CommunSerialPort.BytesToRead < (bIICReadDataLength + 3)
            If sleepdaley > 10 Then
                sleepdaley = 0
                ausUARTRegReadCnt = _CommunSerialPort.BytesToRead
                _CommunSerialPort.Read(aubUARTReadBuf, 0, ausUARTRegReadCnt)  '读取缓冲数据

                Return "串口链接断开"
            End If
            System.Threading.Thread.Sleep(20)
            sleepdaley = sleepdaley + 1
        End While

        ausUARTRegReadCnt = _CommunSerialPort.BytesToRead
        _CommunSerialPort.Read(aubUARTReadBuf, 0, ausUARTRegReadCnt)  '读取缓冲数据

        If (aubUARTReadBuf(0) = 35) And (aubUARTReadBuf(ausUARTRegReadCnt - 1) = 36) Then
            For siFlag = 2 To (ausUARTRegReadCnt - 2)
                aubUARTDrvReadBuf(siFlag - 2) = aubUARTReadBuf(siFlag)
            Next
        Else
            Return "未接入模块"
        End If

        Return "OK"
    End Function

    'IIC 写
    'bIICNumber表示通讯板的IIC号码
    'bIICDeviceAddress表示通讯板IIC链接的模块的IIC地址
    'bIICDataStartAddress表示IIC通讯时写数据起始地址
    'bIICReadDataLength表示IIC通讯时写数据的长度
    '返回值0表示通讯失败，1表示通讯成功，2表示通讯结果异常，但是串口未断开链接
    Public Function STM32UartToIICWriteBytes(ByVal bIICNumber As Byte, _
                                    ByVal bIICDeviceAddress As Byte, _
                                    ByVal bIICDataStartAddress As Byte, _
                                    ByVal bIICWriteDataLength As Integer, _
                                    ByRef aubUARTDrvWriteBuf() As Byte
                                    ) As String

        Dim aubUARTWriteBuf(0 To 255) As Byte
        Dim aubUARTReadBuf(0 To 255) As Byte
        Dim ausUARTRegReadCnt As Integer
        Dim siFlag As Integer

        If (bIICWriteDataLength = 0) Then
            Return "写入数据长度为0"
        End If

        For siFlag = 0 To (bIICWriteDataLength - 1)
            aubUARTWriteBuf(6 + siFlag) = aubUARTDrvWriteBuf(siFlag)
        Next

        aubUARTWriteBuf(0) = Asc("#")                      'Start Byte
        aubUARTWriteBuf(1) = bIICWriteDataLength + 7       'Total Length
        aubUARTWriteBuf(2) = 11                            '0A 读
        aubUARTWriteBuf(3) = bIICNumber                    '扩展IIC编号
        aubUARTWriteBuf(4) = bIICDeviceAddress             'IIC器件地址
        aubUARTWriteBuf(5) = bIICDataStartAddress          '
        aubUARTWriteBuf(bIICWriteDataLength + 6) = Asc("$")                      'Stop Byte


        Try
            _CommunSerialPort.Write(aubUARTWriteBuf, 0, bIICWriteDataLength + 7)
        Catch
            Return "串口链接断开"
        End Try

        Dim sleepdaley As Integer

        While _CommunSerialPort.BytesToRead < 4
            If sleepdaley > 20 Then
                sleepdaley = 0
                ausUARTRegReadCnt = _CommunSerialPort.BytesToRead
                _CommunSerialPort.Read(aubUARTReadBuf, 0, ausUARTRegReadCnt)  '读取缓冲数据

                Return "串口链接断开"
            End If
            System.Threading.Thread.Sleep(20)
            sleepdaley = sleepdaley + 1
        End While

        ausUARTRegReadCnt = _CommunSerialPort.BytesToRead
        _CommunSerialPort.Read(aubUARTReadBuf, 0, ausUARTRegReadCnt)  '读取缓冲数据

        If (aubUARTReadBuf(0) = 35) And (aubUARTReadBuf(ausUARTRegReadCnt - 1) = 36) And (aubUARTReadBuf(2) = 80) Then
            Return "OK"
        Else
            Return "未接入模块"
        End If
        Return "OK"
    End Function

    '切表操作
    'bIICNumber表示通讯板的IIC号码
    'bIICDeviceAddress表示通讯板IIC链接的模块的IIC地址
    'bSelectPage表示需要切到哪个表格
    '返回值0表示通讯失败，1表示通讯成功，2表示通讯结果异常，但是串口未断开链接
    Public Function STM32IICChangePage(ByVal bIICNumber As Byte, ByVal bIICDeviceAddress As Byte, ByVal bSelectPage As Byte) As String

        Dim SelectPageBuf(0) As Byte
        Dim SelectPageBufBak(0) As Byte

        SelectPageBuf(0) = bSelectPage
        SelectPageBufBak(0) = bSelectPage

        If STM32UartToIICWriteBytes(bIICNumber, bIICDeviceAddress, 127, 1, SelectPageBuf) = "OK" Then
            System.Threading.Thread.Sleep(10)
            If STM32UartToIICReadBytes(bIICNumber, bIICDeviceAddress, 127, 1, SelectPageBuf) = "OK" Then
                If SelectPageBuf(0) = SelectPageBufBak(0) Then
                    Return "OK"
                End If
            Else
                Return "NG"
            End If
        Else
            Return "NG"
        End If


        Return "NG"
    End Function




    'IIC 读
    'bIICDeviceAddress表示通讯板IIC链接的模块的IIC地址
    'bIICDataStartAddress表示IIC通讯时读取的数据起始地址
    'bIICReadDataLength表示IIC通讯时读取数据的长度
    'aubUARTDrvReadBuf表示IIC读取的数据缓存
    '返回值0表示通讯失败，1表示通讯成功，2表示通讯结果异常，但是串口未断开链接
    Public Function C8051UartToIICReadBytes(
                                    ByVal bIICDeviceAddress As Byte, _
                                    ByVal bIICDataStartAddress As Byte, _
                                    ByVal bIICReadDataLength As Integer, _
                                    ByRef aubUARTDrvReadBuf() As Byte
                                    ) As String

        Dim aubUARTWriteBuf(0 To 6) As Byte
        Dim aubUARTReadBuf(0 To 255) As Byte
        Dim ausUARTRegReadCnt As Integer
        Dim siFlag As Integer

        If (bIICReadDataLength = 0) Then
            Return "数据长度为0"
        End If

        aubUARTWriteBuf(0) = Asc("#")                      'Start Byte
        aubUARTWriteBuf(1) = 7                             'Total Length
        aubUARTWriteBuf(2) = 6                             '读
        aubUARTWriteBuf(3) = bIICDeviceAddress             'IIC器件地址
        aubUARTWriteBuf(4) = bIICDataStartAddress          '寄存器地址
        aubUARTWriteBuf(5) = bIICReadDataLength            '读取长度
        aubUARTWriteBuf(6) = Asc("$")                      'Stop Byte

        Try
            _CommunSerialPort.Write(aubUARTWriteBuf, 0, 7)
        Catch
            Return "串口链接断开"
        End Try

        Dim sleepdaley As Integer
        System.Threading.Thread.Sleep(60)
        While _CommunSerialPort.BytesToRead < (bIICReadDataLength + 2)
            If sleepdaley > 10 Then
                sleepdaley = 0
                ausUARTRegReadCnt = _CommunSerialPort.BytesToRead
                _CommunSerialPort.Read(aubUARTReadBuf, 0, ausUARTRegReadCnt)  '读取缓冲数据

                Return "串口链接断开"
            End If

            System.Threading.Thread.Sleep(1)
            sleepdaley = sleepdaley + 1
        End While

        ausUARTRegReadCnt = _CommunSerialPort.BytesToRead
        _CommunSerialPort.Read(aubUARTReadBuf, 0, ausUARTRegReadCnt)  '读取缓冲数据

        If (aubUARTReadBuf(0) = 35) And (aubUARTReadBuf(ausUARTRegReadCnt - 1) = 36) Then
            For siFlag = 1 To (ausUARTRegReadCnt - 2)
                aubUARTDrvReadBuf(siFlag - 1) = aubUARTReadBuf(siFlag)
            Next
        Else
            Return "未接入模块"
        End If

        Return "OK"
    End Function

    'IIC 写
    'bIICDeviceAddress表示通讯板IIC链接的模块的IIC地址
    'bIICDataStartAddress表示IIC通讯时写数据起始地址
    'bIICReadDataLength表示IIC通讯时写数据的长度
    'aubUARTDrvReadBuf表示IIC写的数据缓存
    Public Function C8051UartToIICWriteBytes(
                                    ByVal bIICDeviceAddress As Byte, _
                                    ByVal bIICDataStartAddress As Byte, _
                                    ByVal bIICWriteDataLength As Integer, _
                                    ByRef aubUARTDrvWriteBuf() As Byte
                                    ) As String
        Dim aubUARTWriteBuf(0 To 255) As Byte
        Dim aubUARTReadBuf(0 To 255) As Byte
        Dim ausUARTRegReadCnt As Integer
        Dim siFlag As Integer

        If (bIICWriteDataLength = 0) Then
            Return "写入数据长度为0"
        End If

        For siFlag = 0 To (bIICWriteDataLength - 1)
            aubUARTWriteBuf(5 + siFlag) = aubUARTDrvWriteBuf(siFlag)
        Next

        aubUARTWriteBuf(0) = Asc("#")                      'Start Byte
        aubUARTWriteBuf(1) = bIICWriteDataLength + 6       'Total Length
        aubUARTWriteBuf(2) = 7                             '7 写
        aubUARTWriteBuf(3) = bIICDeviceAddress             'IIC器件地址
        aubUARTWriteBuf(4) = bIICDataStartAddress          '
        aubUARTWriteBuf(bIICWriteDataLength + 5) = Asc("$")                      'Stop Byte


        Try
            _CommunSerialPort.Write(aubUARTWriteBuf, 0, bIICWriteDataLength + 6)
        Catch
            Return "串口链接断开"
        End Try

        Dim sleepdaley As Integer
        System.Threading.Thread.Sleep(10)
        While _CommunSerialPort.BytesToRead < 3
            If sleepdaley > 20 Then
                sleepdaley = 0
                ausUARTRegReadCnt = _CommunSerialPort.BytesToRead
                _CommunSerialPort.Read(aubUARTReadBuf, 0, ausUARTRegReadCnt)  '读取缓冲数据
                Return "串口链接断开"
            End If
            System.Threading.Thread.Sleep(2)
            sleepdaley = sleepdaley + 1
        End While

        ausUARTRegReadCnt = _CommunSerialPort.BytesToRead
        _CommunSerialPort.Read(aubUARTReadBuf, 0, ausUARTRegReadCnt)  '读取缓冲数据

        If (aubUARTReadBuf(0) = 35) And (aubUARTReadBuf(ausUARTRegReadCnt - 1) = 36) And (aubUARTReadBuf(1) = 80) Then
            Return "OK"
        Else
            Return "未接入模块"
        End If
        Return "OK"
    End Function

    '切表操作
    'bIICNumber表示通讯板的IIC号码
    'bIICDeviceAddress表示通讯板IIC链接的模块的IIC地址
    'bSelectPage表示需要切到哪个表格
    Public Function C8051IICChangePage(ByVal bIICDeviceAddress As Byte, ByVal bSelectPage As Byte) As String

        Dim SelectPageBuf(0) As Byte
        Dim SelectPageBufBak(0) As Byte

        SelectPageBuf(0) = bSelectPage
        SelectPageBufBak(0) = bSelectPage

        If C8051UartToIICWriteBytes(bIICDeviceAddress, 127, 1, SelectPageBuf) = "OK" Then
            System.Threading.Thread.Sleep(10)
            If C8051UartToIICReadBytes(bIICDeviceAddress, 127, 1, SelectPageBuf) = "OK" Then
                If SelectPageBuf(0) = SelectPageBufBak(0) Then
                    Return "OK"
                End If
            Else

            End If
        Else

        End If

        Return "NG"
    End Function

End Class
