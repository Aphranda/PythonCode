<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class Form1
    Inherits System.Windows.Forms.Form

    'Form 重写 Dispose，以清理组件列表。
    <System.Diagnostics.DebuggerNonUserCode()> _
    Protected Overrides Sub Dispose(ByVal disposing As Boolean)
        Try
            If disposing AndAlso components IsNot Nothing Then
                components.Dispose()
            End If
        Finally
            MyBase.Dispose(disposing)
        End Try
    End Sub

    'Windows 窗体设计器所必需的
    Private components As System.ComponentModel.IContainer

    '注意: 以下过程是 Windows 窗体设计器所必需的
    '可以使用 Windows 窗体设计器修改它。
    '不要使用代码编辑器修改它。
    <System.Diagnostics.DebuggerStepThrough()> _
    Private Sub InitializeComponent()
        Me.components = New System.ComponentModel.Container()
        Me.GroupBox3 = New System.Windows.Forms.GroupBox()
        Me.txtReBit = New System.Windows.Forms.TextBox()
        Me.Label22 = New System.Windows.Forms.Label()
        Me.cmbBit = New System.Windows.Forms.ComboBox()
        Me.Label21 = New System.Windows.Forms.Label()
        Me.txtBitAdd = New System.Windows.Forms.TextBox()
        Me.Label20 = New System.Windows.Forms.Label()
        Me.cmbBitMry = New System.Windows.Forms.ComboBox()
        Me.Label19 = New System.Windows.Forms.Label()
        Me.butBitRst = New System.Windows.Forms.Button()
        Me.butBitSet = New System.Windows.Forms.Button()
        Me.butBitTest = New System.Windows.Forms.Button()
        Me.txtBitTest = New System.Windows.Forms.TextBox()
        Me.Label18 = New System.Windows.Forms.Label()
        Me.txtScanPrd = New System.Windows.Forms.TextBox()
        Me.Label17 = New System.Windows.Forms.Label()
        Me.txtScanCnt = New System.Windows.Forms.TextBox()
        Me.Label16 = New System.Windows.Forms.Label()
        Me.butLink = New System.Windows.Forms.Button()
        Me.Timer1 = New System.Windows.Forms.Timer(Me.components)
        Me.butScan = New System.Windows.Forms.Button()
        Me.butClose = New System.Windows.Forms.Button()
        Me.Label6 = New System.Windows.Forms.Label()
        Me.txtReClose = New System.Windows.Forms.TextBox()
        Me.Label8 = New System.Windows.Forms.Label()
        Me.txtReLink = New System.Windows.Forms.TextBox()
        Me.Label3 = New System.Windows.Forms.Label()
        Me.txtRate = New System.Windows.Forms.TextBox()
        Me.Label2 = New System.Windows.Forms.Label()
        Me.txtPort = New System.Windows.Forms.TextBox()
        Me.Label1 = New System.Windows.Forms.Label()
        Me.txtDelay = New System.Windows.Forms.TextBox()
        Me.Label4 = New System.Windows.Forms.Label()
        Me.txtStation = New System.Windows.Forms.TextBox()
        Me.GroupBox2 = New System.Windows.Forms.GroupBox()
        Me.cmbWriteType = New System.Windows.Forms.ComboBox()
        Me.Label23 = New System.Windows.Forms.Label()
        Me.txtWrite = New System.Windows.Forms.TextBox()
        Me.txtReWrite = New System.Windows.Forms.TextBox()
        Me.Label10 = New System.Windows.Forms.Label()
        Me.butWrite = New System.Windows.Forms.Button()
        Me.cmbWriteMry = New System.Windows.Forms.ComboBox()
        Me.txtWriteAdd = New System.Windows.Forms.TextBox()
        Me.txtWriteCnt = New System.Windows.Forms.TextBox()
        Me.Label13 = New System.Windows.Forms.Label()
        Me.Label14 = New System.Windows.Forms.Label()
        Me.Label15 = New System.Windows.Forms.Label()
        Me.GroupBox1 = New System.Windows.Forms.GroupBox()
        Me.txtReRead = New System.Windows.Forms.TextBox()
        Me.cmbReadType = New System.Windows.Forms.ComboBox()
        Me.Label24 = New System.Windows.Forms.Label()
        Me.Label9 = New System.Windows.Forms.Label()
        Me.butRead = New System.Windows.Forms.Button()
        Me.lstRead = New System.Windows.Forms.ListBox()
        Me.cmbReadMry = New System.Windows.Forms.ComboBox()
        Me.txtReadAdd = New System.Windows.Forms.TextBox()
        Me.txtReadCnt = New System.Windows.Forms.TextBox()
        Me.Label11 = New System.Windows.Forms.Label()
        Me.Label5 = New System.Windows.Forms.Label()
        Me.Label7 = New System.Windows.Forms.Label()
        Me.GroupBox3.SuspendLayout()
        Me.GroupBox2.SuspendLayout()
        Me.GroupBox1.SuspendLayout()
        Me.SuspendLayout()
        '
        'GroupBox3
        '
        Me.GroupBox3.Controls.Add(Me.txtReBit)
        Me.GroupBox3.Controls.Add(Me.Label22)
        Me.GroupBox3.Controls.Add(Me.cmbBit)
        Me.GroupBox3.Controls.Add(Me.Label21)
        Me.GroupBox3.Controls.Add(Me.txtBitAdd)
        Me.GroupBox3.Controls.Add(Me.Label20)
        Me.GroupBox3.Controls.Add(Me.cmbBitMry)
        Me.GroupBox3.Controls.Add(Me.Label19)
        Me.GroupBox3.Controls.Add(Me.butBitRst)
        Me.GroupBox3.Controls.Add(Me.butBitSet)
        Me.GroupBox3.Controls.Add(Me.butBitTest)
        Me.GroupBox3.Controls.Add(Me.txtBitTest)
        Me.GroupBox3.Controls.Add(Me.Label18)
        Me.GroupBox3.Location = New System.Drawing.Point(11, 78)
        Me.GroupBox3.Name = "GroupBox3"
        Me.GroupBox3.Size = New System.Drawing.Size(502, 105)
        Me.GroupBox3.TabIndex = 86
        Me.GroupBox3.TabStop = False
        '
        'txtReBit
        '
        Me.txtReBit.Location = New System.Drawing.Point(423, 23)
        Me.txtReBit.Name = "txtReBit"
        Me.txtReBit.ReadOnly = True
        Me.txtReBit.Size = New System.Drawing.Size(66, 21)
        Me.txtReBit.TabIndex = 61
        Me.txtReBit.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        '
        'Label22
        '
        Me.Label22.AutoSize = True
        Me.Label22.Location = New System.Drawing.Point(374, 27)
        Me.Label22.Name = "Label22"
        Me.Label22.Size = New System.Drawing.Size(41, 12)
        Me.Label22.TabIndex = 62
        Me.Label22.Text = "Return"
        '
        'cmbBit
        '
        Me.cmbBit.FormattingEnabled = True
        Me.cmbBit.Location = New System.Drawing.Point(290, 23)
        Me.cmbBit.Name = "cmbBit"
        Me.cmbBit.Size = New System.Drawing.Size(66, 20)
        Me.cmbBit.TabIndex = 60
        '
        'Label21
        '
        Me.Label21.AutoSize = True
        Me.Label21.Location = New System.Drawing.Point(263, 26)
        Me.Label21.Name = "Label21"
        Me.Label21.Size = New System.Drawing.Size(23, 12)
        Me.Label21.TabIndex = 59
        Me.Label21.Text = "Bit"
        '
        'txtBitAdd
        '
        Me.txtBitAdd.Location = New System.Drawing.Point(197, 23)
        Me.txtBitAdd.Name = "txtBitAdd"
        Me.txtBitAdd.Size = New System.Drawing.Size(50, 21)
        Me.txtBitAdd.TabIndex = 57
        Me.txtBitAdd.Text = "100"
        Me.txtBitAdd.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        '
        'Label20
        '
        Me.Label20.AutoSize = True
        Me.Label20.Location = New System.Drawing.Point(149, 26)
        Me.Label20.Name = "Label20"
        Me.Label20.Size = New System.Drawing.Size(47, 12)
        Me.Label20.TabIndex = 58
        Me.Label20.Text = "Address"
        '
        'cmbBitMry
        '
        Me.cmbBitMry.FormattingEnabled = True
        Me.cmbBitMry.Location = New System.Drawing.Point(62, 23)
        Me.cmbBitMry.Name = "cmbBitMry"
        Me.cmbBitMry.Size = New System.Drawing.Size(66, 20)
        Me.cmbBitMry.TabIndex = 56
        '
        'Label19
        '
        Me.Label19.AutoSize = True
        Me.Label19.Location = New System.Drawing.Point(19, 26)
        Me.Label19.Name = "Label19"
        Me.Label19.Size = New System.Drawing.Size(41, 12)
        Me.Label19.TabIndex = 55
        Me.Label19.Text = "Memory"
        '
        'butBitRst
        '
        Me.butBitRst.Location = New System.Drawing.Point(397, 62)
        Me.butBitRst.Name = "butBitRst"
        Me.butBitRst.Size = New System.Drawing.Size(88, 26)
        Me.butBitRst.TabIndex = 54
        Me.butBitRst.Text = "Bit Reset"
        Me.butBitRst.UseVisualStyleBackColor = True
        '
        'butBitSet
        '
        Me.butBitSet.Location = New System.Drawing.Point(250, 62)
        Me.butBitSet.Name = "butBitSet"
        Me.butBitSet.Size = New System.Drawing.Size(88, 26)
        Me.butBitSet.TabIndex = 53
        Me.butBitSet.Text = "Bit Set"
        Me.butBitSet.UseVisualStyleBackColor = True
        '
        'butBitTest
        '
        Me.butBitTest.Location = New System.Drawing.Point(20, 62)
        Me.butBitTest.Name = "butBitTest"
        Me.butBitTest.Size = New System.Drawing.Size(88, 26)
        Me.butBitTest.TabIndex = 52
        Me.butBitTest.Text = "Bit Test"
        Me.butBitTest.UseVisualStyleBackColor = True
        '
        'txtBitTest
        '
        Me.txtBitTest.Location = New System.Drawing.Point(115, 66)
        Me.txtBitTest.Name = "txtBitTest"
        Me.txtBitTest.ReadOnly = True
        Me.txtBitTest.Size = New System.Drawing.Size(66, 21)
        Me.txtBitTest.TabIndex = 44
        Me.txtBitTest.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        '
        'Label18
        '
        Me.Label18.AutoSize = True
        Me.Label18.Location = New System.Drawing.Point(6, 26)
        Me.Label18.Name = "Label18"
        Me.Label18.Size = New System.Drawing.Size(0, 12)
        Me.Label18.TabIndex = 45
        '
        'txtScanPrd
        '
        Me.txtScanPrd.Location = New System.Drawing.Point(255, 449)
        Me.txtScanPrd.Name = "txtScanPrd"
        Me.txtScanPrd.ReadOnly = True
        Me.txtScanPrd.Size = New System.Drawing.Size(66, 21)
        Me.txtScanPrd.TabIndex = 80
        Me.txtScanPrd.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        '
        'Label17
        '
        Me.Label17.AutoSize = True
        Me.Label17.Location = New System.Drawing.Point(208, 452)
        Me.Label17.Name = "Label17"
        Me.Label17.Size = New System.Drawing.Size(41, 12)
        Me.Label17.TabIndex = 81
        Me.Label17.Text = "Period"
        '
        'txtScanCnt
        '
        Me.txtScanCnt.Location = New System.Drawing.Point(68, 449)
        Me.txtScanCnt.Name = "txtScanCnt"
        Me.txtScanCnt.ReadOnly = True
        Me.txtScanCnt.Size = New System.Drawing.Size(66, 21)
        Me.txtScanCnt.TabIndex = 78
        Me.txtScanCnt.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        '
        'Label16
        '
        Me.Label16.AutoSize = True
        Me.Label16.Location = New System.Drawing.Point(23, 452)
        Me.Label16.Name = "Label16"
        Me.Label16.Size = New System.Drawing.Size(47, 12)
        Me.Label16.TabIndex = 79
        Me.Label16.Text = "Counter"
        '
        'butLink
        '
        Me.butLink.Location = New System.Drawing.Point(422, 9)
        Me.butLink.Name = "butLink"
        Me.butLink.Size = New System.Drawing.Size(88, 26)
        Me.butLink.TabIndex = 63
        Me.butLink.Text = "ComLink"
        Me.butLink.UseVisualStyleBackColor = True
        '
        'Timer1
        '
        '
        'butScan
        '
        Me.butScan.Location = New System.Drawing.Point(412, 443)
        Me.butScan.Name = "butScan"
        Me.butScan.Size = New System.Drawing.Size(88, 30)
        Me.butScan.TabIndex = 65
        Me.butScan.Text = "Cycle R/W"
        Me.butScan.UseVisualStyleBackColor = True
        '
        'butClose
        '
        Me.butClose.Location = New System.Drawing.Point(422, 45)
        Me.butClose.Name = "butClose"
        Me.butClose.Size = New System.Drawing.Size(88, 26)
        Me.butClose.TabIndex = 64
        Me.butClose.Text = "DeLink"
        Me.butClose.UseVisualStyleBackColor = True
        '
        'Label6
        '
        Me.Label6.AutoSize = True
        Me.Label6.Location = New System.Drawing.Point(285, 50)
        Me.Label6.Name = "Label6"
        Me.Label6.Size = New System.Drawing.Size(53, 12)
        Me.Label6.TabIndex = 91
        Me.Label6.Text = "Re.Close"
        '
        'txtReClose
        '
        Me.txtReClose.Location = New System.Drawing.Point(344, 47)
        Me.txtReClose.Name = "txtReClose"
        Me.txtReClose.ReadOnly = True
        Me.txtReClose.Size = New System.Drawing.Size(44, 21)
        Me.txtReClose.TabIndex = 90
        Me.txtReClose.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        '
        'Label8
        '
        Me.Label8.AutoSize = True
        Me.Label8.Location = New System.Drawing.Point(291, 15)
        Me.Label8.Name = "Label8"
        Me.Label8.Size = New System.Drawing.Size(47, 12)
        Me.Label8.TabIndex = 89
        Me.Label8.Text = "Re.Link"
        '
        'txtReLink
        '
        Me.txtReLink.Location = New System.Drawing.Point(344, 12)
        Me.txtReLink.Name = "txtReLink"
        Me.txtReLink.ReadOnly = True
        Me.txtReLink.Size = New System.Drawing.Size(44, 21)
        Me.txtReLink.TabIndex = 88
        Me.txtReLink.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        '
        'Label3
        '
        Me.Label3.AutoSize = True
        Me.Label3.Location = New System.Drawing.Point(14, 49)
        Me.Label3.Name = "Label3"
        Me.Label3.Size = New System.Drawing.Size(59, 12)
        Me.Label3.TabIndex = 87
        Me.Label3.Text = "Comm.Rate"
        '
        'txtRate
        '
        Me.txtRate.Location = New System.Drawing.Point(79, 46)
        Me.txtRate.Name = "txtRate"
        Me.txtRate.Size = New System.Drawing.Size(44, 21)
        Me.txtRate.TabIndex = 86
        Me.txtRate.Text = "9600"
        Me.txtRate.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        '
        'Label2
        '
        Me.Label2.AutoSize = True
        Me.Label2.Location = New System.Drawing.Point(14, 15)
        Me.Label2.Name = "Label2"
        Me.Label2.Size = New System.Drawing.Size(59, 12)
        Me.Label2.TabIndex = 85
        Me.Label2.Text = "Comm.Port"
        '
        'txtPort
        '
        Me.txtPort.Location = New System.Drawing.Point(79, 12)
        Me.txtPort.Name = "txtPort"
        Me.txtPort.Size = New System.Drawing.Size(44, 21)
        Me.txtPort.TabIndex = 84
        Me.txtPort.Text = "2"
        Me.txtPort.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        '
        'Label1
        '
        Me.Label1.AutoSize = True
        Me.Label1.Location = New System.Drawing.Point(171, 48)
        Me.Label1.Name = "Label1"
        Me.Label1.Size = New System.Drawing.Size(35, 12)
        Me.Label1.TabIndex = 95
        Me.Label1.Text = "Delay"
        '
        'txtDelay
        '
        Me.txtDelay.Location = New System.Drawing.Point(214, 45)
        Me.txtDelay.Name = "txtDelay"
        Me.txtDelay.Size = New System.Drawing.Size(44, 21)
        Me.txtDelay.TabIndex = 94
        Me.txtDelay.Text = "200"
        Me.txtDelay.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        '
        'Label4
        '
        Me.Label4.AutoSize = True
        Me.Label4.Location = New System.Drawing.Point(160, 14)
        Me.Label4.Name = "Label4"
        Me.Label4.Size = New System.Drawing.Size(47, 12)
        Me.Label4.TabIndex = 93
        Me.Label4.Text = "Station"
        '
        'txtStation
        '
        Me.txtStation.Location = New System.Drawing.Point(214, 11)
        Me.txtStation.Name = "txtStation"
        Me.txtStation.Size = New System.Drawing.Size(44, 21)
        Me.txtStation.TabIndex = 92
        Me.txtStation.Text = "0"
        Me.txtStation.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        '
        'GroupBox2
        '
        Me.GroupBox2.Controls.Add(Me.cmbWriteType)
        Me.GroupBox2.Controls.Add(Me.Label23)
        Me.GroupBox2.Controls.Add(Me.txtWrite)
        Me.GroupBox2.Controls.Add(Me.txtReWrite)
        Me.GroupBox2.Controls.Add(Me.Label10)
        Me.GroupBox2.Controls.Add(Me.butWrite)
        Me.GroupBox2.Controls.Add(Me.cmbWriteMry)
        Me.GroupBox2.Controls.Add(Me.txtWriteAdd)
        Me.GroupBox2.Controls.Add(Me.txtWriteCnt)
        Me.GroupBox2.Controls.Add(Me.Label13)
        Me.GroupBox2.Controls.Add(Me.Label14)
        Me.GroupBox2.Controls.Add(Me.Label15)
        Me.GroupBox2.Location = New System.Drawing.Point(268, 189)
        Me.GroupBox2.Name = "GroupBox2"
        Me.GroupBox2.Size = New System.Drawing.Size(245, 243)
        Me.GroupBox2.TabIndex = 97
        Me.GroupBox2.TabStop = False
        Me.GroupBox2.Text = "Write"
        '
        'cmbWriteType
        '
        Me.cmbWriteType.FormattingEnabled = True
        Me.cmbWriteType.Location = New System.Drawing.Point(166, 58)
        Me.cmbWriteType.Name = "cmbWriteType"
        Me.cmbWriteType.Size = New System.Drawing.Size(66, 20)
        Me.cmbWriteType.TabIndex = 57
        '
        'Label23
        '
        Me.Label23.AutoSize = True
        Me.Label23.Location = New System.Drawing.Point(133, 63)
        Me.Label23.Name = "Label23"
        Me.Label23.Size = New System.Drawing.Size(29, 12)
        Me.Label23.TabIndex = 55
        Me.Label23.Text = "Type"
        '
        'txtWrite
        '
        Me.txtWrite.Location = New System.Drawing.Point(12, 20)
        Me.txtWrite.Multiline = True
        Me.txtWrite.Name = "txtWrite"
        Me.txtWrite.ScrollBars = System.Windows.Forms.ScrollBars.Vertical
        Me.txtWrite.Size = New System.Drawing.Size(91, 210)
        Me.txtWrite.TabIndex = 54
        '
        'txtReWrite
        '
        Me.txtReWrite.Location = New System.Drawing.Point(166, 168)
        Me.txtReWrite.Name = "txtReWrite"
        Me.txtReWrite.ReadOnly = True
        Me.txtReWrite.Size = New System.Drawing.Size(66, 21)
        Me.txtReWrite.TabIndex = 52
        Me.txtReWrite.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        '
        'Label10
        '
        Me.Label10.AutoSize = True
        Me.Label10.Location = New System.Drawing.Point(121, 171)
        Me.Label10.Name = "Label10"
        Me.Label10.Size = New System.Drawing.Size(41, 12)
        Me.Label10.TabIndex = 53
        Me.Label10.Text = "Return"
        '
        'butWrite
        '
        Me.butWrite.Location = New System.Drawing.Point(144, 203)
        Me.butWrite.Name = "butWrite"
        Me.butWrite.Size = New System.Drawing.Size(88, 26)
        Me.butWrite.TabIndex = 51
        Me.butWrite.Text = "Cmd Write"
        Me.butWrite.UseVisualStyleBackColor = True
        '
        'cmbWriteMry
        '
        Me.cmbWriteMry.FormattingEnabled = True
        Me.cmbWriteMry.Location = New System.Drawing.Point(166, 22)
        Me.cmbWriteMry.Name = "cmbWriteMry"
        Me.cmbWriteMry.Size = New System.Drawing.Size(66, 20)
        Me.cmbWriteMry.TabIndex = 40
        '
        'txtWriteAdd
        '
        Me.txtWriteAdd.Location = New System.Drawing.Point(166, 94)
        Me.txtWriteAdd.Name = "txtWriteAdd"
        Me.txtWriteAdd.Size = New System.Drawing.Size(66, 21)
        Me.txtWriteAdd.TabIndex = 36
        Me.txtWriteAdd.Text = "100"
        Me.txtWriteAdd.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        '
        'txtWriteCnt
        '
        Me.txtWriteCnt.Location = New System.Drawing.Point(166, 131)
        Me.txtWriteCnt.Name = "txtWriteCnt"
        Me.txtWriteCnt.Size = New System.Drawing.Size(66, 21)
        Me.txtWriteCnt.TabIndex = 38
        Me.txtWriteCnt.Text = "1"
        Me.txtWriteCnt.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        '
        'Label13
        '
        Me.Label13.AutoSize = True
        Me.Label13.Location = New System.Drawing.Point(127, 135)
        Me.Label13.Name = "Label13"
        Me.Label13.Size = New System.Drawing.Size(35, 12)
        Me.Label13.TabIndex = 49
        Me.Label13.Text = "Count"
        '
        'Label14
        '
        Me.Label14.AutoSize = True
        Me.Label14.Location = New System.Drawing.Point(121, 27)
        Me.Label14.Name = "Label14"
        Me.Label14.Size = New System.Drawing.Size(41, 12)
        Me.Label14.TabIndex = 39
        Me.Label14.Text = "Memory"
        '
        'Label15
        '
        Me.Label15.AutoSize = True
        Me.Label15.Location = New System.Drawing.Point(114, 99)
        Me.Label15.Name = "Label15"
        Me.Label15.Size = New System.Drawing.Size(47, 12)
        Me.Label15.TabIndex = 43
        Me.Label15.Text = "Address"
        '
        'GroupBox1
        '
        Me.GroupBox1.Controls.Add(Me.txtReRead)
        Me.GroupBox1.Controls.Add(Me.cmbReadType)
        Me.GroupBox1.Controls.Add(Me.Label24)
        Me.GroupBox1.Controls.Add(Me.Label9)
        Me.GroupBox1.Controls.Add(Me.butRead)
        Me.GroupBox1.Controls.Add(Me.lstRead)
        Me.GroupBox1.Controls.Add(Me.cmbReadMry)
        Me.GroupBox1.Controls.Add(Me.txtReadAdd)
        Me.GroupBox1.Controls.Add(Me.txtReadCnt)
        Me.GroupBox1.Controls.Add(Me.Label11)
        Me.GroupBox1.Controls.Add(Me.Label5)
        Me.GroupBox1.Controls.Add(Me.Label7)
        Me.GroupBox1.Location = New System.Drawing.Point(11, 189)
        Me.GroupBox1.Name = "GroupBox1"
        Me.GroupBox1.Size = New System.Drawing.Size(242, 243)
        Me.GroupBox1.TabIndex = 96
        Me.GroupBox1.TabStop = False
        Me.GroupBox1.Text = "Read"
        '
        'txtReRead
        '
        Me.txtReRead.Location = New System.Drawing.Point(161, 168)
        Me.txtReRead.Name = "txtReRead"
        Me.txtReRead.ReadOnly = True
        Me.txtReRead.Size = New System.Drawing.Size(66, 21)
        Me.txtReRead.TabIndex = 52
        Me.txtReRead.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        '
        'cmbReadType
        '
        Me.cmbReadType.FormattingEnabled = True
        Me.cmbReadType.Location = New System.Drawing.Point(161, 58)
        Me.cmbReadType.Name = "cmbReadType"
        Me.cmbReadType.Size = New System.Drawing.Size(66, 20)
        Me.cmbReadType.TabIndex = 58
        '
        'Label24
        '
        Me.Label24.AutoSize = True
        Me.Label24.Location = New System.Drawing.Point(128, 62)
        Me.Label24.Name = "Label24"
        Me.Label24.Size = New System.Drawing.Size(29, 12)
        Me.Label24.TabIndex = 56
        Me.Label24.Text = "Type"
        '
        'Label9
        '
        Me.Label9.AutoSize = True
        Me.Label9.Location = New System.Drawing.Point(116, 170)
        Me.Label9.Name = "Label9"
        Me.Label9.Size = New System.Drawing.Size(41, 12)
        Me.Label9.TabIndex = 53
        Me.Label9.Text = "Return"
        '
        'butRead
        '
        Me.butRead.Location = New System.Drawing.Point(139, 203)
        Me.butRead.Name = "butRead"
        Me.butRead.Size = New System.Drawing.Size(88, 26)
        Me.butRead.TabIndex = 51
        Me.butRead.Text = "Cmd Read"
        Me.butRead.UseVisualStyleBackColor = True
        '
        'lstRead
        '
        Me.lstRead.FormattingEnabled = True
        Me.lstRead.ItemHeight = 12
        Me.lstRead.Location = New System.Drawing.Point(11, 20)
        Me.lstRead.Name = "lstRead"
        Me.lstRead.ScrollAlwaysVisible = True
        Me.lstRead.Size = New System.Drawing.Size(91, 208)
        Me.lstRead.TabIndex = 50
        '
        'cmbReadMry
        '
        Me.cmbReadMry.FormattingEnabled = True
        Me.cmbReadMry.Location = New System.Drawing.Point(161, 22)
        Me.cmbReadMry.Name = "cmbReadMry"
        Me.cmbReadMry.Size = New System.Drawing.Size(66, 20)
        Me.cmbReadMry.TabIndex = 40
        '
        'txtReadAdd
        '
        Me.txtReadAdd.Location = New System.Drawing.Point(161, 94)
        Me.txtReadAdd.Name = "txtReadAdd"
        Me.txtReadAdd.Size = New System.Drawing.Size(66, 21)
        Me.txtReadAdd.TabIndex = 36
        Me.txtReadAdd.Text = "100"
        Me.txtReadAdd.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        '
        'txtReadCnt
        '
        Me.txtReadCnt.Location = New System.Drawing.Point(161, 131)
        Me.txtReadCnt.Name = "txtReadCnt"
        Me.txtReadCnt.Size = New System.Drawing.Size(66, 21)
        Me.txtReadCnt.TabIndex = 38
        Me.txtReadCnt.Text = "5"
        Me.txtReadCnt.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        '
        'Label11
        '
        Me.Label11.AutoSize = True
        Me.Label11.Location = New System.Drawing.Point(122, 134)
        Me.Label11.Name = "Label11"
        Me.Label11.Size = New System.Drawing.Size(35, 12)
        Me.Label11.TabIndex = 49
        Me.Label11.Text = "Count"
        '
        'Label5
        '
        Me.Label5.AutoSize = True
        Me.Label5.Location = New System.Drawing.Point(116, 26)
        Me.Label5.Name = "Label5"
        Me.Label5.Size = New System.Drawing.Size(41, 12)
        Me.Label5.TabIndex = 39
        Me.Label5.Text = "Memory"
        '
        'Label7
        '
        Me.Label7.AutoSize = True
        Me.Label7.Location = New System.Drawing.Point(110, 98)
        Me.Label7.Name = "Label7"
        Me.Label7.Size = New System.Drawing.Size(47, 12)
        Me.Label7.TabIndex = 43
        Me.Label7.Text = "Address"
        '
        'Form1
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 12.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(521, 485)
        Me.Controls.Add(Me.GroupBox2)
        Me.Controls.Add(Me.GroupBox1)
        Me.Controls.Add(Me.Label1)
        Me.Controls.Add(Me.txtDelay)
        Me.Controls.Add(Me.Label4)
        Me.Controls.Add(Me.txtStation)
        Me.Controls.Add(Me.Label6)
        Me.Controls.Add(Me.GroupBox3)
        Me.Controls.Add(Me.txtReClose)
        Me.Controls.Add(Me.txtScanPrd)
        Me.Controls.Add(Me.Label8)
        Me.Controls.Add(Me.Label17)
        Me.Controls.Add(Me.txtReLink)
        Me.Controls.Add(Me.Label3)
        Me.Controls.Add(Me.txtScanCnt)
        Me.Controls.Add(Me.txtRate)
        Me.Controls.Add(Me.Label16)
        Me.Controls.Add(Me.Label2)
        Me.Controls.Add(Me.butLink)
        Me.Controls.Add(Me.txtPort)
        Me.Controls.Add(Me.butScan)
        Me.Controls.Add(Me.butClose)
        Me.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedToolWindow
        Me.Name = "Form1"
        Me.Text = "DLL Testing for OMRON HOSTLINK"
        Me.GroupBox3.ResumeLayout(False)
        Me.GroupBox3.PerformLayout()
        Me.GroupBox2.ResumeLayout(False)
        Me.GroupBox2.PerformLayout()
        Me.GroupBox1.ResumeLayout(False)
        Me.GroupBox1.PerformLayout()
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub
    Friend WithEvents GroupBox3 As System.Windows.Forms.GroupBox
    Friend WithEvents txtReBit As System.Windows.Forms.TextBox
    Friend WithEvents Label22 As System.Windows.Forms.Label
    Friend WithEvents cmbBit As System.Windows.Forms.ComboBox
    Friend WithEvents Label21 As System.Windows.Forms.Label
    Friend WithEvents txtBitAdd As System.Windows.Forms.TextBox
    Friend WithEvents Label20 As System.Windows.Forms.Label
    Friend WithEvents cmbBitMry As System.Windows.Forms.ComboBox
    Friend WithEvents Label19 As System.Windows.Forms.Label
    Friend WithEvents butBitRst As System.Windows.Forms.Button
    Friend WithEvents butBitSet As System.Windows.Forms.Button
    Friend WithEvents butBitTest As System.Windows.Forms.Button
    Friend WithEvents txtBitTest As System.Windows.Forms.TextBox
    Friend WithEvents Label18 As System.Windows.Forms.Label
    Friend WithEvents txtScanPrd As System.Windows.Forms.TextBox
    Friend WithEvents Label17 As System.Windows.Forms.Label
    Friend WithEvents txtScanCnt As System.Windows.Forms.TextBox
    Friend WithEvents Label16 As System.Windows.Forms.Label
    Friend WithEvents butLink As System.Windows.Forms.Button
    Friend WithEvents Timer1 As System.Windows.Forms.Timer
    Friend WithEvents butScan As System.Windows.Forms.Button
    Friend WithEvents butClose As System.Windows.Forms.Button
    Friend WithEvents Label6 As System.Windows.Forms.Label
    Friend WithEvents txtReClose As System.Windows.Forms.TextBox
    Friend WithEvents Label8 As System.Windows.Forms.Label
    Friend WithEvents txtReLink As System.Windows.Forms.TextBox
    Friend WithEvents Label3 As System.Windows.Forms.Label
    Friend WithEvents txtRate As System.Windows.Forms.TextBox
    Friend WithEvents Label2 As System.Windows.Forms.Label
    Friend WithEvents txtPort As System.Windows.Forms.TextBox
    Friend WithEvents Label1 As System.Windows.Forms.Label
    Friend WithEvents txtDelay As System.Windows.Forms.TextBox
    Friend WithEvents Label4 As System.Windows.Forms.Label
    Friend WithEvents txtStation As System.Windows.Forms.TextBox
    Friend WithEvents GroupBox2 As System.Windows.Forms.GroupBox
    Friend WithEvents cmbWriteType As System.Windows.Forms.ComboBox
    Friend WithEvents Label23 As System.Windows.Forms.Label
    Friend WithEvents txtWrite As System.Windows.Forms.TextBox
    Friend WithEvents txtReWrite As System.Windows.Forms.TextBox
    Friend WithEvents Label10 As System.Windows.Forms.Label
    Friend WithEvents butWrite As System.Windows.Forms.Button
    Friend WithEvents cmbWriteMry As System.Windows.Forms.ComboBox
    Friend WithEvents txtWriteAdd As System.Windows.Forms.TextBox
    Friend WithEvents txtWriteCnt As System.Windows.Forms.TextBox
    Friend WithEvents Label13 As System.Windows.Forms.Label
    Friend WithEvents Label14 As System.Windows.Forms.Label
    Friend WithEvents Label15 As System.Windows.Forms.Label
    Friend WithEvents GroupBox1 As System.Windows.Forms.GroupBox
    Friend WithEvents txtReRead As System.Windows.Forms.TextBox
    Friend WithEvents cmbReadType As System.Windows.Forms.ComboBox
    Friend WithEvents Label24 As System.Windows.Forms.Label
    Friend WithEvents Label9 As System.Windows.Forms.Label
    Friend WithEvents butRead As System.Windows.Forms.Button
    Friend WithEvents lstRead As System.Windows.Forms.ListBox
    Friend WithEvents cmbReadMry As System.Windows.Forms.ComboBox
    Friend WithEvents txtReadAdd As System.Windows.Forms.TextBox
    Friend WithEvents txtReadCnt As System.Windows.Forms.TextBox
    Friend WithEvents Label11 As System.Windows.Forms.Label
    Friend WithEvents Label5 As System.Windows.Forms.Label
    Friend WithEvents Label7 As System.Windows.Forms.Label

End Class
