
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


using System.Runtime.InteropServices;

namespace ComTest
{
	public partial class Form1
	{
		public Form1()
		{
			InitializeComponent();
			
		
			if (defaultInstance == null)
				defaultInstance = this;
		}
		
#region Default Instance
		
		private static Form1 defaultInstance;
		

public static Form1 Default
		{
			get
			{
				if (defaultInstance == null)
				{
					defaultInstance = new Form1();
					defaultInstance.FormClosed += new FormClosedEventHandler(defaultInstance_FormClosed);
				}
				
				return defaultInstance;
			}
			set
			{
				defaultInstance = value;
			}
		}
		
		static void defaultInstance_FormClosed(object sender, FormClosedEventArgs e)
		{
			defaultInstance = null;
		}
		
#endregion
		
		HostLink.PlcCom PLC = new HostLink.PlcCom();
		HostLink.PlcCom.PlcMemory CIO = HostLink.PlcCom.PlcMemory.CIO;
		HostLink.PlcCom.PlcMemory LR = HostLink.PlcCom.PlcMemory.LR;
		HostLink.PlcCom.PlcMemory DR = HostLink.PlcCom.PlcMemory.DR;
		HostLink.PlcCom.PlcMemory HR = HostLink.PlcCom.PlcMemory.HR;
		
		bool EntLink;
		long ScanCount;
		
		[DllImport("winmm.dll", ExactSpelling=true, CharSet=CharSet.Ansi, SetLastError=true)]
		public static extern long timeGetTime();
		
		
		public void Form1_Load(System.Object sender, System.EventArgs e)
		{
			short i = 0;
			this.CenterToScreen();
			cmbReadMry.Items.Add("CIO");
			cmbReadMry.Items.Add("LR");
			cmbReadMry.Items.Add("DR");
			cmbReadMry.Items.Add("HR");
			cmbWriteMry.Items.Add("CIO");
			cmbWriteMry.Items.Add("LR");
			cmbWriteMry.Items.Add("DR");
			cmbWriteMry.Items.Add("HR");
			cmbBitMry.Items.Add("CIO");
			cmbBitMry.Items.Add("LR");
			cmbBitMry.Items.Add("DR");
			cmbBitMry.Items.Add("HR");
			for (i = 0; i <= 15; i++)
			{
				cmbBit.Items.Add("Bit" + System.Convert.ToString(i));
			}
			cmbReadType.Items.Clear();
			cmbReadType.Items.Add("INT16");
			cmbReadType.Items.Add("UINT16");
			cmbReadType.Items.Add("DINT32");
			cmbReadType.Items.Add("HEX32");
			cmbReadType.Items.Add("REAL32");
			cmbReadType.Items.Add("BIN16");
            cmbReadType.Items.Add("BCD16");
            cmbReadType.Items.Add("BCD32");
			cmbWriteType.Items.Clear();
			cmbWriteType.Items.Add("INT16");
			cmbWriteType.Items.Add("UINT16");
			cmbWriteType.Items.Add("DINT32");
			cmbWriteType.Items.Add("HEX32");
			cmbWriteType.Items.Add("REAL32");
			cmbWriteType.Items.Add("BIN16");
            cmbWriteType.Items.Add("BCD16");
            cmbWriteType.Items.Add("BCD32");
			cmbReadMry.SelectedIndex = 2;
			cmbWriteMry.SelectedIndex = 2;
			cmbBitMry.SelectedIndex = 0;
			cmbBit.SelectedIndex = 0;
			cmbReadType.SelectedIndex = 0;
			cmbWriteType.SelectedIndex = 0;
			lstRead.Items.Clear();
			txtWrite.Text = "";
		}
		
		public void butLink_Click(System.Object sender, System.EventArgs e)
		{
			short re = 0;
			string restr = "";
            re = PLC.ComLink(Convert.ToUInt16(txtStation.Text), Convert.ToUInt16(txtPort.Text), Convert.ToUInt32(txtRate.Text), 7, 2, HostLink.PlcCom.ParityType.Even, Convert.ToUInt16(txtDelay.Text), "DEMO");
			txtReLink.Text = re.ToString();
			if (re == 0)
			{
				EntLink = true;
				MessageBox.Show("PLC联接成功: " + restr);
			}
			else
			{
				EntLink = false;
				MessageBox.Show("PLC联接失败: " + restr);
			}
		}
		
		public void butClose_Click(System.Object sender, System.EventArgs e)
		{
			short re = 0;
			re = PLC.DeLink();
			txtReClose.Text = re.ToString();
            EntLink = false;
		}
		
		public void butRead_Click(System.Object sender, System.EventArgs e)
		{
			short i = 0;
            short re = 0;
			object[] RD = null;
			RD = new object[Convert.ToInt16(txtReadCnt.Text)];
			if (!EntLink)
			{
				MessageBox.Show("还未与PLC建立联接！");
				return;
			}
			int var1 = cmbReadType.SelectedIndex + 1;
            HostLink.PlcCom.DataType typ = (HostLink.PlcCom.DataType)var1;
			switch (cmbReadMry.SelectedIndex)
			{
				case 0:
                    re = PLC.CmdRead(Convert.ToUInt16(txtStation.Text), CIO, typ, Convert.ToUInt16(txtReadAdd.Text), Convert.ToUInt16(txtReadCnt.Text), ref RD);
					break;
				case 1:
                    re = PLC.CmdRead(Convert.ToUInt16(txtStation.Text), LR, typ, Convert.ToUInt16(txtReadAdd.Text), Convert.ToUInt16(txtReadCnt.Text), ref RD);
					break;
				case 2:
                    re = PLC.CmdRead(Convert.ToUInt16(txtStation.Text), DR, typ, Convert.ToUInt16(txtReadAdd.Text), Convert.ToUInt16(txtReadCnt.Text), ref RD);
					break;
				case 3:
                    re = PLC.CmdRead(Convert.ToUInt16(txtStation.Text), HR, typ, Convert.ToUInt16(txtReadAdd.Text), Convert.ToUInt16(txtReadCnt.Text), ref RD);
					break;
			}
			txtReRead.Text = re.ToString();
			lstRead.Items.Clear();
			for (i = 0; i < RD.Length; i++)
			{
				if (!(RD[i] == null))
				{
					lstRead.Items.Add(RD[i]);
				}
				else
				{
					lstRead.Items.Add("0");
				}
			}
		}
		
		
		public void butWrite_Click(System.Object sender, System.EventArgs e)
		{
			short i = 0;
            short re = 0;
			string[] temp = null;
			object[] WD = null;
			if (!EntLink)
			{
				MessageBox.Show("还未与PLC建立联接！");
				return;
			}
            WD = new object[Convert.ToUInt16(txtWriteCnt.Text)];
			temp = txtWrite.Text.Split('\n');
			for (i = 0; i < WD.Length; i++)
			{
				if (i >= temp.Length )
				{
					WD[i] = 0;
				}
				else
				{
					WD[i] = temp[i].Trim();
				}
			}
			int var1 = cmbWriteType.SelectedIndex + 1;
			HostLink.PlcCom.DataType typ =(HostLink.PlcCom.DataType) var1;
			switch (cmbWriteMry.SelectedIndex)
			{
				case 0:
                    re = PLC.CmdWrite(Convert.ToUInt16(txtStation.Text), CIO, typ, Convert.ToUInt16(txtWriteAdd.Text), Convert.ToUInt16(txtWriteCnt.Text), ref WD);
					break;
				case 1:
                    re = PLC.CmdWrite(Convert.ToUInt16(txtStation.Text), LR, typ, Convert.ToUInt16(txtWriteAdd.Text), Convert.ToUInt16(txtWriteCnt.Text), ref WD);
					break;
				case 2:
                    re = PLC.CmdWrite(Convert.ToUInt16(txtStation.Text), DR, typ, Convert.ToUInt16(txtWriteAdd.Text), Convert.ToUInt16(txtWriteCnt.Text), ref WD);
					break;
				case 3:
                    re = PLC.CmdWrite(Convert.ToUInt16(txtStation.Text), HR, typ, Convert.ToUInt16(txtWriteAdd.Text), Convert.ToUInt16(txtWriteCnt.Text), ref WD);
					break;
			}
			txtReWrite.Text = re.ToString();
		}
		
		public void butScan_Click(System.Object sender, System.EventArgs e)
		{
			if (!EntLink)
			{
				MessageBox.Show("还未与PLC建立联接！");
				return;
			}
			if (butScan.Text == "Cycle R/W")
			{
				ScanCount = 0;
				Timer1.Enabled = true;
				butScan.Text = "Stop R/W";
			}
			else
			{
				Timer1.Enabled = false;
				butScan.Text = "Cycle R/W";
			}
		}
		
		public void Timer1_Tick(System.Object sender, System.EventArgs e)
		{
            Timer1.Enabled = false;
            int tim = System.Convert.ToInt32(timeGetTime());
            if (!EntLink)
            {
                MessageBox.Show("还未与PLC建立联接！");
                return;
            }
            //
            butRead_Click(null, null);
            butWrite_Click(null, null);

            //
            if ((Convert.ToInt32(txtReRead.Text) < 0) || (Convert.ToInt32(txtReWrite.Text) < 0))
            {
                butScan.Text = "Cycle R/W";
                return;
            }
            else
            {
                ScanCount++;
                txtScanCnt.Text = ScanCount.ToString();
                txtScanPrd.Text = (System.Convert.ToInt32(timeGetTime()) - tim).ToString() + "ms";
            }
            Timer1.Enabled = true;
		}
		
		
		public void butBitTest_Click(System.Object sender, System.EventArgs e)
		{
			if (!EntLink)
			{
				MessageBox.Show("还未与PLC建立联接！");
				return;
			}
			bool rd = false;
			short re = 0;
			switch (cmbBitMry.SelectedIndex)
			{
				case 0:
                    re = PLC.Bit_Test(Convert.ToUInt16(txtStation.Text), CIO, Convert.ToUInt16(txtBitAdd.Text), Convert.ToUInt16(cmbBit.SelectedIndex), ref rd);
					break;
				case 1:
					re = PLC.Bit_Test(Convert.ToUInt16(txtStation.Text), LR, Convert.ToUInt16(txtBitAdd.Text), Convert.ToUInt16(cmbBit.SelectedIndex), ref rd);
					break;
				case 2:
					re = PLC.Bit_Test(Convert.ToUInt16(txtStation.Text), DR, Convert.ToUInt16(txtBitAdd.Text), Convert.ToUInt16(cmbBit.SelectedIndex), ref rd);
					break;
				case 3:
					re = PLC.Bit_Test(Convert.ToUInt16(txtStation.Text), HR, Convert.ToUInt16(txtBitAdd.Text), Convert.ToUInt16(cmbBit.SelectedIndex), ref rd);
					break;
			}
			txtBitTest.Text = System.Convert.ToString(rd);
			txtReBit.Text = re.ToString();
		}
		
		public void butBitSet_Click(System.Object sender, System.EventArgs e)
		{
			if (!EntLink)
			{
				MessageBox.Show("还未与PLC建立联接！");
				return;
			}
			short re = 0;
			switch (cmbBitMry.SelectedIndex)
			{
				case 0:
					re = PLC.Bit_Set(Convert.ToUInt16(txtStation.Text), CIO, Convert.ToUInt16(txtBitAdd.Text), Convert.ToUInt16(cmbBit.SelectedIndex));
					break;
				case 1:
					re = PLC.Bit_Set(Convert.ToUInt16(txtStation.Text), LR, Convert.ToUInt16(txtBitAdd.Text), Convert.ToUInt16(cmbBit.SelectedIndex));
					break;
				case 2:
					re = PLC.Bit_Set(Convert.ToUInt16(txtStation.Text), DR, Convert.ToUInt16(txtBitAdd.Text), Convert.ToUInt16(cmbBit.SelectedIndex));
					break;
				case 3:
					re = PLC.Bit_Set(Convert.ToUInt16(txtStation.Text), HR, Convert.ToUInt16(txtBitAdd.Text), Convert.ToUInt16(cmbBit.SelectedIndex));
					break;
			}
			txtReBit.Text = re.ToString();
		}
		
		public void butBitRst_Click(System.Object sender, System.EventArgs e)
		{
			if (!EntLink)
			{
				MessageBox.Show("还未与PLC建立联接！");
				return;
			}
			short re = 0;
			switch (cmbBitMry.SelectedIndex)
			{
				case 0:
					re = PLC.Bit_Reset(Convert.ToUInt16(txtStation.Text), CIO, Convert.ToUInt16(txtBitAdd.Text), Convert.ToUInt16(cmbBit.SelectedIndex));
					break;
				case 1:
					re = PLC.Bit_Reset(Convert.ToUInt16(txtStation.Text), LR, Convert.ToUInt16(txtBitAdd.Text), Convert.ToUInt16(cmbBit.SelectedIndex));
					break;
				case 2:
					re = PLC.Bit_Reset(Convert.ToUInt16(txtStation.Text), DR, Convert.ToUInt16(txtBitAdd.Text), Convert.ToUInt16(cmbBit.SelectedIndex));
					break;
				case 3:
					re = PLC.Bit_Reset(Convert.ToUInt16(txtStation.Text), HR, Convert.ToUInt16(txtBitAdd.Text),Convert.ToUInt16( cmbBit.SelectedIndex));
					break;
			}
			txtReBit.Text = re.ToString();
		}
		
		
	}
	
}
