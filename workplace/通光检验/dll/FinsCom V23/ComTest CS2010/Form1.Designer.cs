
using System.Collections.Generic;
using System;
using System.Linq;
using System.Drawing;
using System.Diagnostics;
using System.Data;
using System.Xml.Linq;
using Microsoft.VisualBasic;
using System.Collections;
using System.Windows.Forms;



namespace ComTest
{
	[global::Microsoft.VisualBasic.CompilerServices.DesignerGenerated()]public 
	partial class Form1 : System.Windows.Forms.Form
	{
		
		//Form 重写 Dispose，以清理组件列表。
		[System.Diagnostics.DebuggerNonUserCode()]protected override void Dispose(bool disposing)
		{
			try
			{
				if (disposing && components != null)
				{
					components.Dispose();
				}
			}
			finally
			{
				base.Dispose(disposing);
			}
		}
		
		//Windows 窗体设计器所必需的
		private System.ComponentModel.Container components = null;
		
		//注意: 以下过程是 Windows 窗体设计器所必需的
		//可以使用 Windows 窗体设计器修改它。
		//不要使用代码编辑器修改它。
		[System.Diagnostics.DebuggerStepThrough()]private void InitializeComponent()
		{
			this.components = new System.ComponentModel.Container();
			base.Load += new System.EventHandler(Form1_Load);
			this.GroupBox3 = new System.Windows.Forms.GroupBox();
			this.txtReBit = new System.Windows.Forms.TextBox();
			this.Label22 = new System.Windows.Forms.Label();
			this.cmbBit = new System.Windows.Forms.ComboBox();
			this.Label21 = new System.Windows.Forms.Label();
			this.txtBitAdd = new System.Windows.Forms.TextBox();
			this.Label20 = new System.Windows.Forms.Label();
			this.cmbBitMry = new System.Windows.Forms.ComboBox();
			this.Label19 = new System.Windows.Forms.Label();
			this.butBitRst = new System.Windows.Forms.Button();
			this.butBitRst.Click += new System.EventHandler(this.butBitRst_Click);
			this.butBitSet = new System.Windows.Forms.Button();
			this.butBitSet.Click += new System.EventHandler(this.butBitSet_Click);
			this.butBitTest = new System.Windows.Forms.Button();
			this.butBitTest.Click += new System.EventHandler(this.butBitTest_Click);
			this.txtBitTest = new System.Windows.Forms.TextBox();
			this.Label18 = new System.Windows.Forms.Label();
			this.txtScanPrd = new System.Windows.Forms.TextBox();
			this.Label17 = new System.Windows.Forms.Label();
			this.txtScanCnt = new System.Windows.Forms.TextBox();
			this.Label16 = new System.Windows.Forms.Label();
			this.butLink = new System.Windows.Forms.Button();
			this.butLink.Click += new System.EventHandler(this.butLink_Click);
			this.Timer1 = new System.Windows.Forms.Timer(this.components);
			this.Timer1.Tick += new System.EventHandler(this.Timer1_Tick);
			this.butScan = new System.Windows.Forms.Button();
			this.butScan.Click += new System.EventHandler(this.butScan_Click);
			this.butClose = new System.Windows.Forms.Button();
			this.butClose.Click += new System.EventHandler(this.butClose_Click);
			this.Label6 = new System.Windows.Forms.Label();
			this.txtReClose = new System.Windows.Forms.TextBox();
			this.Label8 = new System.Windows.Forms.Label();
			this.txtReLink = new System.Windows.Forms.TextBox();
			this.Label3 = new System.Windows.Forms.Label();
			this.txtRate = new System.Windows.Forms.TextBox();
			this.Label2 = new System.Windows.Forms.Label();
			this.txtPort = new System.Windows.Forms.TextBox();
			this.Label1 = new System.Windows.Forms.Label();
			this.txtDelay = new System.Windows.Forms.TextBox();
			this.Label4 = new System.Windows.Forms.Label();
			this.txtStation = new System.Windows.Forms.TextBox();
			this.GroupBox2 = new System.Windows.Forms.GroupBox();
			this.cmbWriteType = new System.Windows.Forms.ComboBox();
			this.Label23 = new System.Windows.Forms.Label();
			this.txtWrite = new System.Windows.Forms.TextBox();
			this.txtReWrite = new System.Windows.Forms.TextBox();
			this.Label10 = new System.Windows.Forms.Label();
			this.butWrite = new System.Windows.Forms.Button();
			this.butWrite.Click += new System.EventHandler(this.butWrite_Click);
			this.cmbWriteMry = new System.Windows.Forms.ComboBox();
			this.txtWriteAdd = new System.Windows.Forms.TextBox();
			this.txtWriteCnt = new System.Windows.Forms.TextBox();
			this.Label13 = new System.Windows.Forms.Label();
			this.Label14 = new System.Windows.Forms.Label();
			this.Label15 = new System.Windows.Forms.Label();
			this.GroupBox1 = new System.Windows.Forms.GroupBox();
			this.txtReRead = new System.Windows.Forms.TextBox();
			this.cmbReadType = new System.Windows.Forms.ComboBox();
			this.Label24 = new System.Windows.Forms.Label();
			this.Label9 = new System.Windows.Forms.Label();
			this.butRead = new System.Windows.Forms.Button();
			this.butRead.Click += new System.EventHandler(this.butRead_Click);
			this.lstRead = new System.Windows.Forms.ListBox();
			this.cmbReadMry = new System.Windows.Forms.ComboBox();
			this.txtReadAdd = new System.Windows.Forms.TextBox();
			this.txtReadCnt = new System.Windows.Forms.TextBox();
			this.Label11 = new System.Windows.Forms.Label();
			this.Label5 = new System.Windows.Forms.Label();
			this.Label7 = new System.Windows.Forms.Label();
			this.GroupBox7 = new System.Windows.Forms.GroupBox();
			this.txtReWriteString = new System.Windows.Forms.TextBox();
			this.txtWriteString = new System.Windows.Forms.TextBox();
			this.butReadString = new System.Windows.Forms.Button();
			this.butReadString.Click += new System.EventHandler(this.butReadString_Click);
			this.butWriteString = new System.Windows.Forms.Button();
			this.butWriteString.Click += new System.EventHandler(this.butWriteString_Click);
			this.txtBuffAdd = new System.Windows.Forms.TextBox();
			this.Label59 = new System.Windows.Forms.Label();
			this.txtBuffSize = new System.Windows.Forms.TextBox();
			this.Label58 = new System.Windows.Forms.Label();
			this.txtReadString = new System.Windows.Forms.TextBox();
			this.GroupBox3.SuspendLayout();
			this.GroupBox2.SuspendLayout();
			this.GroupBox1.SuspendLayout();
			this.GroupBox7.SuspendLayout();
			this.SuspendLayout();
			//
			//GroupBox3
			//
			this.GroupBox3.Controls.Add(this.txtReBit);
			this.GroupBox3.Controls.Add(this.Label22);
			this.GroupBox3.Controls.Add(this.cmbBit);
			this.GroupBox3.Controls.Add(this.Label21);
			this.GroupBox3.Controls.Add(this.txtBitAdd);
			this.GroupBox3.Controls.Add(this.Label20);
			this.GroupBox3.Controls.Add(this.cmbBitMry);
			this.GroupBox3.Controls.Add(this.Label19);
			this.GroupBox3.Controls.Add(this.butBitRst);
			this.GroupBox3.Controls.Add(this.butBitSet);
			this.GroupBox3.Controls.Add(this.butBitTest);
			this.GroupBox3.Controls.Add(this.txtBitTest);
			this.GroupBox3.Controls.Add(this.Label18);
			this.GroupBox3.Location = new System.Drawing.Point(11, 78);
			this.GroupBox3.Name = "GroupBox3";
			this.GroupBox3.Size = new System.Drawing.Size(502, 105);
			this.GroupBox3.TabIndex = 86;
			this.GroupBox3.TabStop = false;
			//
			//txtReBit
			//
			this.txtReBit.Location = new System.Drawing.Point(423, 23);
			this.txtReBit.Name = "txtReBit";
			this.txtReBit.ReadOnly = true;
			this.txtReBit.Size = new System.Drawing.Size(66, 21);
			this.txtReBit.TabIndex = 61;
			this.txtReBit.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
			//
			//Label22
			//
			this.Label22.AutoSize = true;
			this.Label22.Location = new System.Drawing.Point(374, 27);
			this.Label22.Name = "Label22";
			this.Label22.Size = new System.Drawing.Size(41, 12);
			this.Label22.TabIndex = 62;
			this.Label22.Text = "Return";
			//
			//cmbBit
			//
			this.cmbBit.FormattingEnabled = true;
			this.cmbBit.Location = new System.Drawing.Point(309, 23);
			this.cmbBit.Name = "cmbBit";
			this.cmbBit.Size = new System.Drawing.Size(47, 20);
			this.cmbBit.TabIndex = 60;
			//
			//Label21
			//
			this.Label21.AutoSize = true;
			this.Label21.Location = new System.Drawing.Point(281, 26);
			this.Label21.Name = "Label21";
			this.Label21.Size = new System.Drawing.Size(23, 12);
			this.Label21.TabIndex = 59;
			this.Label21.Text = "Bit";
			//
			//txtBitAdd
			//
			this.txtBitAdd.Location = new System.Drawing.Point(197, 23);
			this.txtBitAdd.Name = "txtBitAdd";
			this.txtBitAdd.Size = new System.Drawing.Size(50, 21);
			this.txtBitAdd.TabIndex = 57;
			this.txtBitAdd.Text = "1";
			this.txtBitAdd.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
			//
			//Label20
			//
			this.Label20.AutoSize = true;
			this.Label20.Location = new System.Drawing.Point(144, 26);
			this.Label20.Name = "Label20";
			this.Label20.Size = new System.Drawing.Size(47, 12);
			this.Label20.TabIndex = 58;
			this.Label20.Text = "Address";
			//
			//cmbBitMry
			//
			this.cmbBitMry.FormattingEnabled = true;
			this.cmbBitMry.Location = new System.Drawing.Point(62, 23);
			this.cmbBitMry.Name = "cmbBitMry";
			this.cmbBitMry.Size = new System.Drawing.Size(46, 20);
			this.cmbBitMry.TabIndex = 56;
			//
			//Label19
			//
			this.Label19.AutoSize = true;
			this.Label19.Location = new System.Drawing.Point(19, 26);
			this.Label19.Name = "Label19";
			this.Label19.Size = new System.Drawing.Size(41, 12);
			this.Label19.TabIndex = 55;
			this.Label19.Text = "Memory";
			//
			//butBitRst
			//
			this.butBitRst.Location = new System.Drawing.Point(397, 62);
			this.butBitRst.Name = "butBitRst";
			this.butBitRst.Size = new System.Drawing.Size(88, 26);
			this.butBitRst.TabIndex = 54;
			this.butBitRst.Text = "Bit Reset";
			this.butBitRst.UseVisualStyleBackColor = true;
			//
			//butBitSet
			//
			this.butBitSet.Location = new System.Drawing.Point(250, 62);
			this.butBitSet.Name = "butBitSet";
			this.butBitSet.Size = new System.Drawing.Size(88, 26);
			this.butBitSet.TabIndex = 53;
			this.butBitSet.Text = "Bit Set";
			this.butBitSet.UseVisualStyleBackColor = true;
			//
			//butBitTest
			//
			this.butBitTest.Location = new System.Drawing.Point(20, 62);
			this.butBitTest.Name = "butBitTest";
			this.butBitTest.Size = new System.Drawing.Size(88, 26);
			this.butBitTest.TabIndex = 52;
			this.butBitTest.Text = "Bit Test";
			this.butBitTest.UseVisualStyleBackColor = true;
			//
			//txtBitTest
			//
			this.txtBitTest.Location = new System.Drawing.Point(115, 66);
			this.txtBitTest.Name = "txtBitTest";
			this.txtBitTest.ReadOnly = true;
			this.txtBitTest.Size = new System.Drawing.Size(66, 21);
			this.txtBitTest.TabIndex = 44;
			this.txtBitTest.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
			//
			//Label18
			//
			this.Label18.AutoSize = true;
			this.Label18.Location = new System.Drawing.Point(6, 26);
			this.Label18.Name = "Label18";
			this.Label18.Size = new System.Drawing.Size(0, 12);
			this.Label18.TabIndex = 45;
			//
			//txtScanPrd
			//
			this.txtScanPrd.Location = new System.Drawing.Point(255, 449);
			this.txtScanPrd.Name = "txtScanPrd";
			this.txtScanPrd.ReadOnly = true;
			this.txtScanPrd.Size = new System.Drawing.Size(66, 21);
			this.txtScanPrd.TabIndex = 80;
			this.txtScanPrd.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
			//
			//Label17
			//
			this.Label17.AutoSize = true;
			this.Label17.Location = new System.Drawing.Point(208, 452);
			this.Label17.Name = "Label17";
			this.Label17.Size = new System.Drawing.Size(41, 12);
			this.Label17.TabIndex = 81;
			this.Label17.Text = "Period";
			//
			//txtScanCnt
			//
			this.txtScanCnt.Location = new System.Drawing.Point(68, 449);
			this.txtScanCnt.Name = "txtScanCnt";
			this.txtScanCnt.ReadOnly = true;
			this.txtScanCnt.Size = new System.Drawing.Size(66, 21);
			this.txtScanCnt.TabIndex = 78;
			this.txtScanCnt.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
			//
			//Label16
			//
			this.Label16.AutoSize = true;
			this.Label16.Location = new System.Drawing.Point(23, 452);
			this.Label16.Name = "Label16";
			this.Label16.Size = new System.Drawing.Size(47, 12);
			this.Label16.TabIndex = 79;
			this.Label16.Text = "Counter";
			//
			//butLink
			//
			this.butLink.Location = new System.Drawing.Point(618, 9);
			this.butLink.Name = "butLink";
			this.butLink.Size = new System.Drawing.Size(88, 26);
			this.butLink.TabIndex = 63;
			this.butLink.Text = "ComLink";
			this.butLink.UseVisualStyleBackColor = true;
			//
			//Timer1
			//
			//
			//butScan
			//
			this.butScan.Location = new System.Drawing.Point(412, 443);
			this.butScan.Name = "butScan";
			this.butScan.Size = new System.Drawing.Size(88, 30);
			this.butScan.TabIndex = 65;
			this.butScan.Text = "Cycle R/W";
			this.butScan.UseVisualStyleBackColor = true;
			//
			//butClose
			//
			this.butClose.Location = new System.Drawing.Point(618, 45);
			this.butClose.Name = "butClose";
			this.butClose.Size = new System.Drawing.Size(88, 26);
			this.butClose.TabIndex = 64;
			this.butClose.Text = "DeLink";
			this.butClose.UseVisualStyleBackColor = true;
			//
			//Label6
			//
			this.Label6.AutoSize = true;
			this.Label6.Location = new System.Drawing.Point(420, 51);
			this.Label6.Name = "Label6";
			this.Label6.Size = new System.Drawing.Size(59, 12);
			this.Label6.TabIndex = 91;
			this.Label6.Text = "Re.DeLink";
			//
			//txtReClose
			//
			this.txtReClose.Location = new System.Drawing.Point(488, 47);
			this.txtReClose.Name = "txtReClose";
			this.txtReClose.ReadOnly = true;
			this.txtReClose.Size = new System.Drawing.Size(44, 21);
			this.txtReClose.TabIndex = 90;
			this.txtReClose.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
			//
			//Label8
			//
			this.Label8.AutoSize = true;
			this.Label8.Location = new System.Drawing.Point(426, 16);
			this.Label8.Name = "Label8";
			this.Label8.Size = new System.Drawing.Size(47, 12);
			this.Label8.TabIndex = 89;
			this.Label8.Text = "Re.Link";
			//
			//txtReLink
			//
			this.txtReLink.Location = new System.Drawing.Point(488, 12);
			this.txtReLink.Name = "txtReLink";
			this.txtReLink.ReadOnly = true;
			this.txtReLink.Size = new System.Drawing.Size(44, 21);
			this.txtReLink.TabIndex = 88;
			this.txtReLink.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
			//
			//Label3
			//
			this.Label3.AutoSize = true;
			this.Label3.Location = new System.Drawing.Point(14, 49);
			this.Label3.Name = "Label3";
			this.Label3.Size = new System.Drawing.Size(59, 12);
			this.Label3.TabIndex = 87;
			this.Label3.Text = "Comm.Rate";
			//
			//txtRate
			//
			this.txtRate.Location = new System.Drawing.Point(95, 46);
			this.txtRate.Name = "txtRate";
			this.txtRate.Size = new System.Drawing.Size(44, 21);
			this.txtRate.TabIndex = 86;
			this.txtRate.Text = "9600";
			this.txtRate.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
			//
			//Label2
			//
			this.Label2.AutoSize = true;
			this.Label2.Location = new System.Drawing.Point(14, 15);
			this.Label2.Name = "Label2";
			this.Label2.Size = new System.Drawing.Size(59, 12);
			this.Label2.TabIndex = 85;
			this.Label2.Text = "Comm.Port";
			//
			//txtPort
			//
			this.txtPort.Location = new System.Drawing.Point(95, 12);
			this.txtPort.Name = "txtPort";
			this.txtPort.Size = new System.Drawing.Size(44, 21);
			this.txtPort.TabIndex = 84;
			this.txtPort.Text = "1";
			this.txtPort.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
			//
			//Label1
			//
			this.Label1.AutoSize = true;
			this.Label1.Location = new System.Drawing.Point(239, 50);
			this.Label1.Name = "Label1";
			this.Label1.Size = new System.Drawing.Size(35, 12);
			this.Label1.TabIndex = 95;
			this.Label1.Text = "Delay";
			//
			//txtDelay
			//
			this.txtDelay.Location = new System.Drawing.Point(292, 46);
			this.txtDelay.Name = "txtDelay";
			this.txtDelay.Size = new System.Drawing.Size(44, 21);
			this.txtDelay.TabIndex = 94;
			this.txtDelay.Text = "2000";
			this.txtDelay.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
			//
			//Label4
			//
			this.Label4.AutoSize = true;
			this.Label4.Location = new System.Drawing.Point(228, 16);
			this.Label4.Name = "Label4";
			this.Label4.Size = new System.Drawing.Size(47, 12);
			this.Label4.TabIndex = 93;
			this.Label4.Text = "Station";
			//
			//txtStation
			//
			this.txtStation.Location = new System.Drawing.Point(292, 12);
			this.txtStation.Name = "txtStation";
			this.txtStation.Size = new System.Drawing.Size(44, 21);
			this.txtStation.TabIndex = 92;
			this.txtStation.Text = "1";
			this.txtStation.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
			//
			//GroupBox2
			//
			this.GroupBox2.Controls.Add(this.cmbWriteType);
			this.GroupBox2.Controls.Add(this.Label23);
			this.GroupBox2.Controls.Add(this.txtWrite);
			this.GroupBox2.Controls.Add(this.txtReWrite);
			this.GroupBox2.Controls.Add(this.Label10);
			this.GroupBox2.Controls.Add(this.butWrite);
			this.GroupBox2.Controls.Add(this.cmbWriteMry);
			this.GroupBox2.Controls.Add(this.txtWriteAdd);
			this.GroupBox2.Controls.Add(this.txtWriteCnt);
			this.GroupBox2.Controls.Add(this.Label13);
			this.GroupBox2.Controls.Add(this.Label14);
			this.GroupBox2.Controls.Add(this.Label15);
			this.GroupBox2.Location = new System.Drawing.Point(268, 189);
			this.GroupBox2.Name = "GroupBox2";
			this.GroupBox2.Size = new System.Drawing.Size(245, 243);
			this.GroupBox2.TabIndex = 97;
			this.GroupBox2.TabStop = false;
			this.GroupBox2.Text = "Write";
			//
			//cmbWriteType
			//
			this.cmbWriteType.FormattingEnabled = true;
			this.cmbWriteType.Location = new System.Drawing.Point(166, 58);
			this.cmbWriteType.Name = "cmbWriteType";
			this.cmbWriteType.Size = new System.Drawing.Size(66, 20);
			this.cmbWriteType.TabIndex = 57;
			//
			//Label23
			//
			this.Label23.AutoSize = true;
			this.Label23.Location = new System.Drawing.Point(133, 63);
			this.Label23.Name = "Label23";
			this.Label23.Size = new System.Drawing.Size(29, 12);
			this.Label23.TabIndex = 55;
			this.Label23.Text = "Type";
			//
			//txtWrite
			//
			this.txtWrite.Location = new System.Drawing.Point(12, 20);
			this.txtWrite.Multiline = true;
			this.txtWrite.Name = "txtWrite";
			this.txtWrite.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
			this.txtWrite.Size = new System.Drawing.Size(91, 210);
			this.txtWrite.TabIndex = 54;
			//
			//txtReWrite
			//
			this.txtReWrite.Location = new System.Drawing.Point(166, 168);
			this.txtReWrite.Name = "txtReWrite";
			this.txtReWrite.ReadOnly = true;
			this.txtReWrite.Size = new System.Drawing.Size(66, 21);
			this.txtReWrite.TabIndex = 52;
			this.txtReWrite.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
			//
			//Label10
			//
			this.Label10.AutoSize = true;
			this.Label10.Location = new System.Drawing.Point(121, 171);
			this.Label10.Name = "Label10";
			this.Label10.Size = new System.Drawing.Size(41, 12);
			this.Label10.TabIndex = 53;
			this.Label10.Text = "Return";
			//
			//butWrite
			//
			this.butWrite.Location = new System.Drawing.Point(144, 203);
			this.butWrite.Name = "butWrite";
			this.butWrite.Size = new System.Drawing.Size(88, 26);
			this.butWrite.TabIndex = 51;
			this.butWrite.Text = "Cmd Write";
			this.butWrite.UseVisualStyleBackColor = true;
			//
			//cmbWriteMry
			//
			this.cmbWriteMry.FormattingEnabled = true;
			this.cmbWriteMry.Location = new System.Drawing.Point(166, 22);
			this.cmbWriteMry.Name = "cmbWriteMry";
			this.cmbWriteMry.Size = new System.Drawing.Size(66, 20);
			this.cmbWriteMry.TabIndex = 40;
			//
			//txtWriteAdd
			//
			this.txtWriteAdd.Location = new System.Drawing.Point(166, 94);
			this.txtWriteAdd.Name = "txtWriteAdd";
			this.txtWriteAdd.Size = new System.Drawing.Size(66, 21);
			this.txtWriteAdd.TabIndex = 36;
			this.txtWriteAdd.Text = "0";
			this.txtWriteAdd.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
			//
			//txtWriteCnt
			//
			this.txtWriteCnt.Location = new System.Drawing.Point(166, 131);
			this.txtWriteCnt.Name = "txtWriteCnt";
			this.txtWriteCnt.Size = new System.Drawing.Size(66, 21);
			this.txtWriteCnt.TabIndex = 38;
			this.txtWriteCnt.Text = "1";
			this.txtWriteCnt.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
			//
			//Label13
			//
			this.Label13.AutoSize = true;
			this.Label13.Location = new System.Drawing.Point(127, 135);
			this.Label13.Name = "Label13";
			this.Label13.Size = new System.Drawing.Size(35, 12);
			this.Label13.TabIndex = 49;
			this.Label13.Text = "Count";
			//
			//Label14
			//
			this.Label14.AutoSize = true;
			this.Label14.Location = new System.Drawing.Point(121, 27);
			this.Label14.Name = "Label14";
			this.Label14.Size = new System.Drawing.Size(41, 12);
			this.Label14.TabIndex = 39;
			this.Label14.Text = "Memory";
			//
			//Label15
			//
			this.Label15.AutoSize = true;
			this.Label15.Location = new System.Drawing.Point(114, 99);
			this.Label15.Name = "Label15";
			this.Label15.Size = new System.Drawing.Size(47, 12);
			this.Label15.TabIndex = 43;
			this.Label15.Text = "Address";
			//
			//GroupBox1
			//
			this.GroupBox1.Controls.Add(this.txtReRead);
			this.GroupBox1.Controls.Add(this.cmbReadType);
			this.GroupBox1.Controls.Add(this.Label24);
			this.GroupBox1.Controls.Add(this.Label9);
			this.GroupBox1.Controls.Add(this.butRead);
			this.GroupBox1.Controls.Add(this.lstRead);
			this.GroupBox1.Controls.Add(this.cmbReadMry);
			this.GroupBox1.Controls.Add(this.txtReadAdd);
			this.GroupBox1.Controls.Add(this.txtReadCnt);
			this.GroupBox1.Controls.Add(this.Label11);
			this.GroupBox1.Controls.Add(this.Label5);
			this.GroupBox1.Controls.Add(this.Label7);
			this.GroupBox1.Location = new System.Drawing.Point(11, 189);
			this.GroupBox1.Name = "GroupBox1";
			this.GroupBox1.Size = new System.Drawing.Size(242, 243);
			this.GroupBox1.TabIndex = 96;
			this.GroupBox1.TabStop = false;
			this.GroupBox1.Text = "Read";
			//
			//txtReRead
			//
			this.txtReRead.Location = new System.Drawing.Point(161, 168);
			this.txtReRead.Name = "txtReRead";
			this.txtReRead.ReadOnly = true;
			this.txtReRead.Size = new System.Drawing.Size(66, 21);
			this.txtReRead.TabIndex = 52;
			this.txtReRead.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
			//
			//cmbReadType
			//
			this.cmbReadType.FormattingEnabled = true;
			this.cmbReadType.Location = new System.Drawing.Point(161, 58);
			this.cmbReadType.Name = "cmbReadType";
			this.cmbReadType.Size = new System.Drawing.Size(66, 20);
			this.cmbReadType.TabIndex = 58;
			//
			//Label24
			//
			this.Label24.AutoSize = true;
			this.Label24.Location = new System.Drawing.Point(128, 62);
			this.Label24.Name = "Label24";
			this.Label24.Size = new System.Drawing.Size(29, 12);
			this.Label24.TabIndex = 56;
			this.Label24.Text = "Type";
			//
			//Label9
			//
			this.Label9.AutoSize = true;
			this.Label9.Location = new System.Drawing.Point(116, 170);
			this.Label9.Name = "Label9";
			this.Label9.Size = new System.Drawing.Size(41, 12);
			this.Label9.TabIndex = 53;
			this.Label9.Text = "Return";
			//
			//butRead
			//
			this.butRead.Location = new System.Drawing.Point(139, 203);
			this.butRead.Name = "butRead";
			this.butRead.Size = new System.Drawing.Size(88, 26);
			this.butRead.TabIndex = 51;
			this.butRead.Text = "Cmd Read";
			this.butRead.UseVisualStyleBackColor = true;
			//
			//lstRead
			//
			this.lstRead.FormattingEnabled = true;
			this.lstRead.ItemHeight = 12;
			this.lstRead.Location = new System.Drawing.Point(11, 20);
			this.lstRead.Name = "lstRead";
			this.lstRead.ScrollAlwaysVisible = true;
			this.lstRead.Size = new System.Drawing.Size(91, 208);
			this.lstRead.TabIndex = 50;
			//
			//cmbReadMry
			//
			this.cmbReadMry.FormattingEnabled = true;
			this.cmbReadMry.Location = new System.Drawing.Point(161, 22);
			this.cmbReadMry.Name = "cmbReadMry";
			this.cmbReadMry.Size = new System.Drawing.Size(66, 20);
			this.cmbReadMry.TabIndex = 40;
			//
			//txtReadAdd
			//
			this.txtReadAdd.Location = new System.Drawing.Point(161, 94);
			this.txtReadAdd.Name = "txtReadAdd";
			this.txtReadAdd.Size = new System.Drawing.Size(66, 21);
			this.txtReadAdd.TabIndex = 36;
			this.txtReadAdd.Text = "0";
			this.txtReadAdd.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
			//
			//txtReadCnt
			//
			this.txtReadCnt.Location = new System.Drawing.Point(161, 131);
			this.txtReadCnt.Name = "txtReadCnt";
			this.txtReadCnt.Size = new System.Drawing.Size(66, 21);
			this.txtReadCnt.TabIndex = 38;
			this.txtReadCnt.Text = "5";
			this.txtReadCnt.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
			//
			//Label11
			//
			this.Label11.AutoSize = true;
			this.Label11.Location = new System.Drawing.Point(122, 134);
			this.Label11.Name = "Label11";
			this.Label11.Size = new System.Drawing.Size(35, 12);
			this.Label11.TabIndex = 49;
			this.Label11.Text = "Count";
			//
			//Label5
			//
			this.Label5.AutoSize = true;
			this.Label5.Location = new System.Drawing.Point(116, 26);
			this.Label5.Name = "Label5";
			this.Label5.Size = new System.Drawing.Size(41, 12);
			this.Label5.TabIndex = 39;
			this.Label5.Text = "Memory";
			//
			//Label7
			//
			this.Label7.AutoSize = true;
			this.Label7.Location = new System.Drawing.Point(110, 98);
			this.Label7.Name = "Label7";
			this.Label7.Size = new System.Drawing.Size(47, 12);
			this.Label7.TabIndex = 43;
			this.Label7.Text = "Address";
			//
			//GroupBox7
			//
			this.GroupBox7.Controls.Add(this.txtReWriteString);
			this.GroupBox7.Controls.Add(this.txtWriteString);
			this.GroupBox7.Controls.Add(this.butReadString);
			this.GroupBox7.Controls.Add(this.butWriteString);
			this.GroupBox7.Controls.Add(this.txtBuffAdd);
			this.GroupBox7.Controls.Add(this.Label59);
			this.GroupBox7.Controls.Add(this.txtBuffSize);
			this.GroupBox7.Controls.Add(this.Label58);
			this.GroupBox7.Controls.Add(this.txtReadString);
			this.GroupBox7.Location = new System.Drawing.Point(528, 82);
			this.GroupBox7.Name = "GroupBox7";
			this.GroupBox7.Size = new System.Drawing.Size(179, 382);
			this.GroupBox7.TabIndex = 108;
			this.GroupBox7.TabStop = false;
			this.GroupBox7.Text = "String R/W (DM Area)";
			//
			//txtReWriteString
			//
			this.txtReWriteString.Location = new System.Drawing.Point(15, 346);
			this.txtReWriteString.Name = "txtReWriteString";
			this.txtReWriteString.ReadOnly = true;
			this.txtReWriteString.Size = new System.Drawing.Size(36, 21);
			this.txtReWriteString.TabIndex = 122;
			this.txtReWriteString.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
			//
			//txtWriteString
			//
			this.txtWriteString.Location = new System.Drawing.Point(15, 258);
			this.txtWriteString.Multiline = true;
			this.txtWriteString.Name = "txtWriteString";
			this.txtWriteString.ScrollBars = System.Windows.Forms.ScrollBars.Horizontal;
			this.txtWriteString.Size = new System.Drawing.Size(151, 75);
			this.txtWriteString.TabIndex = 121;
			this.txtWriteString.Text = "String is OK";
			//
			//butReadString
			//
			this.butReadString.Location = new System.Drawing.Point(57, 214);
			this.butReadString.Name = "butReadString";
			this.butReadString.Size = new System.Drawing.Size(109, 26);
			this.butReadString.TabIndex = 120;
			this.butReadString.Text = "CmdReadString";
			this.butReadString.UseVisualStyleBackColor = true;
			//
			//butWriteString
			//
			this.butWriteString.Location = new System.Drawing.Point(57, 344);
			this.butWriteString.Name = "butWriteString";
			this.butWriteString.Size = new System.Drawing.Size(109, 26);
			this.butWriteString.TabIndex = 119;
			this.butWriteString.Text = "CmdWriteString";
			this.butWriteString.UseVisualStyleBackColor = true;
			//
			//txtBuffAdd
			//
			this.txtBuffAdd.Location = new System.Drawing.Point(103, 36);
			this.txtBuffAdd.Name = "txtBuffAdd";
			this.txtBuffAdd.Size = new System.Drawing.Size(63, 21);
			this.txtBuffAdd.TabIndex = 117;
			this.txtBuffAdd.Text = "100";
			this.txtBuffAdd.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
			//
			//Label59
			//
			this.Label59.AutoSize = true;
			this.Label59.Location = new System.Drawing.Point(13, 44);
			this.Label59.Name = "Label59";
			this.Label59.Size = new System.Drawing.Size(47, 12);
			this.Label59.TabIndex = 118;
			this.Label59.Text = "Address";
			//
			//txtBuffSize
			//
			this.txtBuffSize.Location = new System.Drawing.Point(103, 78);
			this.txtBuffSize.Name = "txtBuffSize";
			this.txtBuffSize.Size = new System.Drawing.Size(63, 21);
			this.txtBuffSize.TabIndex = 115;
			this.txtBuffSize.Text = "20";
			this.txtBuffSize.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
			//
			//Label58
			//
			this.Label58.AutoSize = true;
			this.Label58.Location = new System.Drawing.Point(13, 81);
			this.Label58.Name = "Label58";
			this.Label58.Size = new System.Drawing.Size(71, 12);
			this.Label58.TabIndex = 116;
			this.Label58.Text = "String Size";
			//
			//txtReadString
			//
			this.txtReadString.Location = new System.Drawing.Point(15, 128);
			this.txtReadString.Multiline = true;
			this.txtReadString.Name = "txtReadString";
			this.txtReadString.ReadOnly = true;
			this.txtReadString.ScrollBars = System.Windows.Forms.ScrollBars.Horizontal;
			this.txtReadString.Size = new System.Drawing.Size(151, 75);
			this.txtReadString.TabIndex = 111;
			//
			//Form1
			//
			this.AutoScaleDimensions = new System.Drawing.SizeF((float) (6.0F), (float) (12.0F));
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.ClientSize = new System.Drawing.Size(718, 485);
			this.Controls.Add(this.GroupBox7);
			this.Controls.Add(this.txtReClose);
			this.Controls.Add(this.txtReLink);
			this.Controls.Add(this.GroupBox2);
			this.Controls.Add(this.GroupBox1);
			this.Controls.Add(this.Label1);
			this.Controls.Add(this.txtDelay);
			this.Controls.Add(this.Label4);
			this.Controls.Add(this.txtStation);
			this.Controls.Add(this.Label6);
			this.Controls.Add(this.GroupBox3);
			this.Controls.Add(this.txtScanPrd);
			this.Controls.Add(this.Label8);
			this.Controls.Add(this.Label17);
			this.Controls.Add(this.Label3);
			this.Controls.Add(this.txtScanCnt);
			this.Controls.Add(this.txtRate);
			this.Controls.Add(this.Label16);
			this.Controls.Add(this.Label2);
			this.Controls.Add(this.butLink);
			this.Controls.Add(this.txtPort);
			this.Controls.Add(this.butScan);
			this.Controls.Add(this.butClose);
			this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedToolWindow;
			this.Name = "Form1";
			this.Text = "DLL Testing for OMRON FINS/COM ";
			this.GroupBox3.ResumeLayout(false);
			this.GroupBox3.PerformLayout();
			this.GroupBox2.ResumeLayout(false);
			this.GroupBox2.PerformLayout();
			this.GroupBox1.ResumeLayout(false);
			this.GroupBox1.PerformLayout();
			this.GroupBox7.ResumeLayout(false);
			this.GroupBox7.PerformLayout();
			this.ResumeLayout(false);
			this.PerformLayout();
			
		}
		internal System.Windows.Forms.GroupBox GroupBox3;
		internal System.Windows.Forms.TextBox txtReBit;
		internal System.Windows.Forms.Label Label22;
		internal System.Windows.Forms.ComboBox cmbBit;
		internal System.Windows.Forms.Label Label21;
		internal System.Windows.Forms.TextBox txtBitAdd;
		internal System.Windows.Forms.Label Label20;
		internal System.Windows.Forms.ComboBox cmbBitMry;
		internal System.Windows.Forms.Label Label19;
		internal System.Windows.Forms.Button butBitRst;
		internal System.Windows.Forms.Button butBitSet;
		internal System.Windows.Forms.Button butBitTest;
		internal System.Windows.Forms.TextBox txtBitTest;
		internal System.Windows.Forms.Label Label18;
		internal System.Windows.Forms.TextBox txtScanPrd;
		internal System.Windows.Forms.Label Label17;
		internal System.Windows.Forms.TextBox txtScanCnt;
		internal System.Windows.Forms.Label Label16;
		internal System.Windows.Forms.Button butLink;
		internal System.Windows.Forms.Timer Timer1;
		internal System.Windows.Forms.Button butScan;
		internal System.Windows.Forms.Button butClose;
		internal System.Windows.Forms.Label Label6;
		internal System.Windows.Forms.TextBox txtReClose;
		internal System.Windows.Forms.Label Label8;
		internal System.Windows.Forms.TextBox txtReLink;
		internal System.Windows.Forms.Label Label3;
		internal System.Windows.Forms.TextBox txtRate;
		internal System.Windows.Forms.Label Label2;
		internal System.Windows.Forms.TextBox txtPort;
		internal System.Windows.Forms.Label Label1;
		internal System.Windows.Forms.TextBox txtDelay;
		internal System.Windows.Forms.Label Label4;
		internal System.Windows.Forms.TextBox txtStation;
		internal System.Windows.Forms.GroupBox GroupBox2;
		internal System.Windows.Forms.ComboBox cmbWriteType;
		internal System.Windows.Forms.Label Label23;
		internal System.Windows.Forms.TextBox txtWrite;
		internal System.Windows.Forms.TextBox txtReWrite;
		internal System.Windows.Forms.Label Label10;
		internal System.Windows.Forms.Button butWrite;
		internal System.Windows.Forms.ComboBox cmbWriteMry;
		internal System.Windows.Forms.TextBox txtWriteAdd;
		internal System.Windows.Forms.TextBox txtWriteCnt;
		internal System.Windows.Forms.Label Label13;
		internal System.Windows.Forms.Label Label14;
		internal System.Windows.Forms.Label Label15;
		internal System.Windows.Forms.GroupBox GroupBox1;
		internal System.Windows.Forms.TextBox txtReRead;
		internal System.Windows.Forms.ComboBox cmbReadType;
		internal System.Windows.Forms.Label Label24;
		internal System.Windows.Forms.Label Label9;
		internal System.Windows.Forms.Button butRead;
		internal System.Windows.Forms.ListBox lstRead;
		internal System.Windows.Forms.ComboBox cmbReadMry;
		internal System.Windows.Forms.TextBox txtReadAdd;
		internal System.Windows.Forms.TextBox txtReadCnt;
		internal System.Windows.Forms.Label Label11;
		internal System.Windows.Forms.Label Label5;
		internal System.Windows.Forms.Label Label7;
		internal System.Windows.Forms.GroupBox GroupBox7;
		internal System.Windows.Forms.TextBox txtReWriteString;
		internal System.Windows.Forms.TextBox txtWriteString;
		internal System.Windows.Forms.Button butReadString;
		internal System.Windows.Forms.Button butWriteString;
		internal System.Windows.Forms.TextBox txtBuffAdd;
		internal System.Windows.Forms.Label Label59;
		internal System.Windows.Forms.TextBox txtBuffSize;
		internal System.Windows.Forms.Label Label58;
		internal System.Windows.Forms.TextBox txtReadString;
		
	}
	
}
