Public Class Form1

    Dim PLC As New HostLink.PlcCom
    Dim CIO As HostLink.PlcCom.PlcMemory = HostLink.PlcCom.PlcMemory.CIO
    Dim LR As HostLink.PlcCom.PlcMemory = HostLink.PlcCom.PlcMemory.LR
    Dim DR As HostLink.PlcCom.PlcMemory = HostLink.PlcCom.PlcMemory.DR
    Dim HR As HostLink.PlcCom.PlcMemory = HostLink.PlcCom.PlcMemory.HR

    Dim EntLink As Boolean
    Dim ScanCount As Long


    Declare Function timeGetTime Lib "winmm.dll" () As Long


    Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
        Dim i As Short
        Me.CenterToScreen()
        cmbReadMry.Items.Add("CIO")
        cmbReadMry.Items.Add("LR")
        cmbReadMry.Items.Add("DR")
        cmbReadMry.Items.Add("HR")
        cmbWriteMry.Items.Add("CIO")
        cmbWriteMry.Items.Add("LR")
        cmbWriteMry.Items.Add("DR")
        cmbWriteMry.Items.Add("HR")
        cmbBitMry.Items.Add("CIO")
        cmbBitMry.Items.Add("LR")
        cmbBitMry.Items.Add("DR")
        cmbBitMry.Items.Add("HR")
        For i = 0 To 15 Step 1
            cmbBit.Items.Add("Bit" & i)
        Next i
        cmbReadType.Items.Clear()
        cmbReadType.Items.Add("INT16")
        cmbReadType.Items.Add("UINT16")
        cmbReadType.Items.Add("DINT32")
        cmbReadType.Items.Add("HEX32")
        cmbReadType.Items.Add("REAL32")
        cmbReadType.Items.Add("BIN16")
        cmbReadType.Items.Add("BCD16")
        cmbReadType.Items.Add("BCD32")
        cmbWriteType.Items.Clear()
        cmbWriteType.Items.Add("INT16")
        cmbWriteType.Items.Add("UINT16")
        cmbWriteType.Items.Add("DINT32")
        cmbWriteType.Items.Add("HEX32")
        cmbWriteType.Items.Add("REAL32")
        cmbWriteType.Items.Add("BIN16")
        cmbWriteType.Items.Add("BCD16")
        cmbWriteType.Items.Add("BCD32")
        cmbReadMry.SelectedIndex = 2
        cmbWriteMry.SelectedIndex = 2
        cmbBitMry.SelectedIndex = 0
        cmbBit.SelectedIndex = 0
        cmbReadType.SelectedIndex = 0
        cmbWriteType.SelectedIndex = 0
        lstRead.Items.Clear()
        txtWrite.Text = ""
    End Sub

    Private Sub butLink_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles butLink.Click
        Dim re As Short
        Dim restr As String = ""
        re = PLC.ComLink(Val(txtStation.Text), Trim(txtPort.Text), Val(txtRate.Text), 7, 2, HostLink.PlcCom.ParityType.Even, Val(txtDelay.Text), "DEMO")
        txtReLink.Text = re.ToString
        If re = 0 Then
            EntLink = True
            MsgBox("PLC联接成功: " & restr)
        Else
            EntLink = False
            MsgBox("PLC联接失败: " & restr)
        End If
    End Sub

    Private Sub butClose_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles butClose.Click
        Dim re As Short
        re = PLC.DeLink()
        txtReClose.Text = re.ToString
        EntLink = False
    End Sub

    Private Sub butRead_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles butRead.Click
        Dim i As Short
        Dim re As Short
        Dim RD() As Object
        ReDim RD(Val(txtReadCnt.Text - 1))
        If Not EntLink Then
            MsgBox("还未与PLC建立联接！")
            Exit Sub
        End If
        Dim var1 As Integer = cmbReadType.SelectedIndex + 1
        Dim typ As HostLink.PlcCom.DataType = var1
        Select Case cmbReadMry.SelectedIndex
            Case 0 : re = PLC.CmdRead(Val(txtStation.Text), CIO, typ, Val(txtReadAdd.Text), Val(txtReadCnt.Text), RD)
            Case 1 : re = PLC.CmdRead(Val(txtStation.Text), LR, typ, Val(txtReadAdd.Text), Val(txtReadCnt.Text), RD)
            Case 2 : re = PLC.CmdRead(Val(txtStation.Text), DR, typ, Val(txtReadAdd.Text), Val(txtReadCnt.Text), RD)
            Case 3 : re = PLC.CmdRead(Val(txtStation.Text), HR, typ, Val(txtReadAdd.Text), Val(txtReadCnt.Text), RD)
        End Select
        txtReRead.Text = re.ToString
        lstRead.Items.Clear()
        For i = 0 To UBound(RD) Step 1
            If Not IsNothing(RD(i)) Then
                lstRead.Items.Add(RD(i))
            Else
                lstRead.Items.Add("0")
            End If
        Next i
    End Sub


    Private Sub butWrite_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles butWrite.Click
        Dim i As Short
        Dim re As Short
        Dim temp() As String
        Dim WD() As Object
        If Not EntLink Then
            MsgBox("还未与PLC建立联接！")
            Exit Sub
        End If
        ReDim WD(Val(txtWriteCnt.Text) - 1)
        temp = Split(txtWrite.Text, vbCrLf)
        For i = 0 To UBound(WD) Step 1
            If i > UBound(temp) Then
                WD(i) = 0
            Else
                WD(i) = Trim(temp(i))
            End If
        Next i
        Dim var1 As Integer = cmbWriteType.SelectedIndex + 1
        Dim typ As HostLink.PlcCom.DataType = var1
        Select Case cmbWriteMry.SelectedIndex
            Case 0 : re = PLC.CmdWrite(Val(txtStation.Text), CIO, typ, Val(txtWriteAdd.Text), Val(txtWriteCnt.Text), WD)
            Case 1 : re = PLC.CmdWrite(Val(txtStation.Text), LR, typ, Val(txtWriteAdd.Text), Val(txtWriteCnt.Text), WD)
            Case 2 : re = PLC.CmdWrite(Val(txtStation.Text), DR, typ, Val(txtWriteAdd.Text), Val(txtWriteCnt.Text), WD)
            Case 3 : re = PLC.CmdWrite(Val(txtStation.Text), HR, typ, Val(txtWriteAdd.Text), Val(txtWriteCnt.Text), WD)
        End Select
        txtReWrite.Text = re.ToString
    End Sub

    Private Sub butScan_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles butScan.Click
        If Not EntLink Then
            MsgBox("还未与PLC建立联接！")
            Exit Sub
        End If
        If butScan.Text = "Cycle R/W" Then
            ScanCount = 0
            Timer1.Enabled = True
            butScan.Text = "Stop R/W"
        Else
            Timer1.Enabled = False
            butScan.Text = "Cycle R/W"
        End If
    End Sub

    Private Sub Timer1_Tick(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Timer1.Tick
        Timer1.Enabled = False
        Dim tim As Integer = timeGetTime
        If Not EntLink Then
            MsgBox("还未与PLC建立联接！")
            Exit Sub
        End If
        '
        Call butRead_Click(Nothing, Nothing)
        Call butWrite_Click(Nothing, Nothing)
        '
        If (Val(txtReRead.Text) < 0) Or (Val(txtReWrite.Text) < 0) Then
            butScan.Text = "Cycle R/W"
            Exit Sub
        Else
            ScanCount += 1
            txtScanCnt.Text = ScanCount
            txtScanPrd.Text = (timeGetTime - tim) & "ms"
        End If
        Timer1.Enabled = True
    End Sub


    Private Sub butBitTest_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles butBitTest.Click
        If Not EntLink Then
            MsgBox("还未与PLC建立联接！")
            Exit Sub
        End If
        Dim rd As Boolean
        Dim re As Short
        Select Case cmbBitMry.SelectedIndex
            Case 0 : re = PLC.Bit_Test(Val(txtStation.Text), CIO, Val(txtBitAdd.Text), cmbBit.SelectedIndex, rd)
            Case 1 : re = PLC.Bit_Test(Val(txtStation.Text), LR, Val(txtBitAdd.Text), cmbBit.SelectedIndex, rd)
            Case 2 : re = PLC.Bit_Test(Val(txtStation.Text), DR, Val(txtBitAdd.Text), cmbBit.SelectedIndex, rd)
            Case 3 : re = PLC.Bit_Test(Val(txtStation.Text), HR, Val(txtBitAdd.Text), cmbBit.SelectedIndex, rd)
        End Select
        txtBitTest.Text = rd
        txtReBit.Text = re
    End Sub

    Private Sub butBitSet_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles butBitSet.Click
        If Not EntLink Then
            MsgBox("还未与PLC建立联接！")
            Exit Sub
        End If
        Dim re As Short
        Select Case cmbBitMry.SelectedIndex
            Case 0 : re = PLC.Bit_Set(Val(txtStation.Text), CIO, Val(txtBitAdd.Text), cmbBit.SelectedIndex)
            Case 1 : re = PLC.Bit_Set(Val(txtStation.Text), LR, Val(txtBitAdd.Text), cmbBit.SelectedIndex)
            Case 2 : re = PLC.Bit_Set(Val(txtStation.Text), DR, Val(txtBitAdd.Text), cmbBit.SelectedIndex)
            Case 3 : re = PLC.Bit_Set(Val(txtStation.Text), HR, Val(txtBitAdd.Text), cmbBit.SelectedIndex)
        End Select
        txtReBit.Text = re
    End Sub

    Private Sub butBitRst_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles butBitRst.Click
        If Not EntLink Then
            MsgBox("还未与PLC建立联接！")
            Exit Sub
        End If
        Dim re As Short
        Select Case cmbBitMry.SelectedIndex
            Case 0 : re = PLC.Bit_Reset(Val(txtStation.Text), CIO, Val(txtBitAdd.Text), cmbBit.SelectedIndex)
            Case 1 : re = PLC.Bit_Reset(Val(txtStation.Text), LR, Val(txtBitAdd.Text), cmbBit.SelectedIndex)
            Case 2 : re = PLC.Bit_Reset(Val(txtStation.Text), DR, Val(txtBitAdd.Text), cmbBit.SelectedIndex)
            Case 2 : re = PLC.Bit_Reset(Val(txtStation.Text), HR, Val(txtBitAdd.Text), cmbBit.SelectedIndex)
        End Select
        txtReBit.Text = re
    End Sub


End Class
