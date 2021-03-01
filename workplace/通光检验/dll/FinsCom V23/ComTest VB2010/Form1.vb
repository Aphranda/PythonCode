Public Class Form1

    Dim PLC As New FinsCom.PlcCom
    Dim EntLink As Boolean
    Dim ScanCount As Long


    Declare Function timeGetTime Lib "winmm.dll" () As Long


    Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
        Dim i As Short
        Me.CenterToScreen()
        cmbReadMry.Items.Add("CIO")
        cmbReadMry.Items.Add("WR")
        cmbReadMry.Items.Add("HR")
        cmbReadMry.Items.Add("DM")
        cmbReadMry.Items.Add("EM")

        cmbWriteMry.Items.Add("CIO")
        cmbWriteMry.Items.Add("WR")
        cmbWriteMry.Items.Add("HR")
        cmbWriteMry.Items.Add("DM")
        cmbWriteMry.Items.Add("EM")

        cmbBitMry.Items.Add("CIO")
        cmbBitMry.Items.Add("WR")
        cmbBitMry.Items.Add("HR")
        cmbBitMry.Items.Add("DM")
        cmbBitMry.Items.Add("EM")
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

        cmbReadMry.SelectedIndex = 3
        cmbWriteMry.SelectedIndex = 3
        cmbBitMry.SelectedIndex = 1
        cmbBit.SelectedIndex = 0
        cmbReadType.SelectedIndex = 0
        cmbWriteType.SelectedIndex = 0
        lstRead.Items.Clear()
        txtWrite.Text = ""
    End Sub

    Private Sub butLink_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles butLink.Click
        Dim re As Short
        Dim restr As String = ""
        re = PLC.ComLink(Trim(txtPort.Text), Val(txtRate.Text), 7, 2, FinsCom.PlcCom.ParityType.Even, Val(txtDelay.Text), "DEMO")
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
        If Not EntLink Then
            MsgBox("还未与PLC建立联接！")
            Exit Sub
        End If
        re = PLC.DeLink()
        txtReClose.Text = re.ToString
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
        Dim var1 As Integer = cmbReadMry.SelectedIndex + 1
        Dim mry As FinsCom.PlcCom.PlcMemory = var1
        var1 = cmbReadType.SelectedIndex + 1
        Dim typ As FinsCom.PlcCom.DataType = var1

        re = PLC.CmdRead(CUShort(txtStation.Text), mry, typ, CUShort(txtReadAdd.Text), CUShort(txtReadCnt.Text), RD)

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
        Dim var1 As Integer = cmbWriteMry.SelectedIndex + 1
        Dim mry As FinsCom.PlcCom.PlcMemory = var1
        var1 = cmbWriteType.SelectedIndex + 1
        Dim typ As FinsCom.PlcCom.DataType = var1

        re = PLC.CmdWrite(CUShort(txtStation.Text), mry, typ, CUShort(txtWriteAdd.Text), CUShort(txtWriteCnt.Text), WD)

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
            txtScanCnt.Text = ScanCount.ToString
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
        Dim var1 As Integer = cmbBitMry.SelectedIndex + 1
        Dim mry As FinsCom.PlcCom.PlcMemory = var1

        re = PLC.Bit_Test(CUShort(txtStation.Text), mry, CUShort(txtBitAdd.Text), CUShort(cmbBit.SelectedIndex), rd)

        txtBitTest.Text = rd
        txtReBit.Text = re
    End Sub

    Private Sub butBitSet_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles butBitSet.Click
        If Not EntLink Then
            MsgBox("还未与PLC建立联接！")
            Exit Sub
        End If
        Dim re As Short
        Dim var1 As Integer = cmbBitMry.SelectedIndex + 1
        Dim mry As FinsCom.PlcCom.PlcMemory = var1
        re = PLC.Bit_Set(CUShort(txtStation.Text), mry, Val(txtBitAdd.Text), cmbBit.SelectedIndex)

        txtReBit.Text = re
    End Sub

    Private Sub butBitRst_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles butBitRst.Click
        If Not EntLink Then
            MsgBox("还未与PLC建立联接！")
            Exit Sub
        End If
        Dim re As Short
        Dim var1 As Integer = cmbBitMry.SelectedIndex + 1
        Dim mry As FinsCom.PlcCom.PlcMemory = var1

        re = PLC.Bit_Reset(CUShort(txtStation.Text), mry, CUShort(txtBitAdd.Text), CUShort(cmbBit.SelectedIndex))

        txtReBit.Text = re
    End Sub

    Private Sub butReadString_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles butReadString.Click
        If Not EntLink Then
            MsgBox("还未与PLC建立联接！")
            Exit Sub
        End If
        Dim re As String
        re = PLC.CmdReadString(CUShort(txtStation.Text), FinsCom.PlcCom.PlcMemory.DR, CShort(txtBuffAdd.Text), CShort(txtBuffSize.Text))
        txtReadString.Text = re
    End Sub

    Private Sub butWriteString_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles butWriteString.Click
        If Not EntLink Then
            MsgBox("还未与PLC建立联接！")
            Exit Sub
        End If
        Dim re As Short
        re = PLC.CmdWriteString(CUShort(txtStation.Text), FinsCom.PlcCom.PlcMemory.DR, CShort(txtBuffAdd.Text), CShort(txtBuffSize.Text), txtWriteString.Text)
        txtReWriteString.Text = re.ToString
    End Sub
End Class
