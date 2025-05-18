namespace Sample
{
    partial class UDDualTransfer
    {
        /// <summary>
        /// 必要なデザイナー変数です。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 使用中のリソースをすべてクリーンアップします。
        /// </summary>
        /// <param name="disposing">マネージド リソースを破棄する場合は true を指定し、その他の場合は false を指定します。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows フォーム デザイナーで生成されたコード

        /// <summary>
        /// デザイナー サポートに必要なメソッドです。このメソッドの内容を
        /// コード エディターで変更しないでください。
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(UDDualTransfer));
            this.listView = new System.Windows.Forms.ListView();
            this.label2 = new System.Windows.Forms.Label();
            this.btn_download = new System.Windows.Forms.Button();
            this.label4 = new System.Windows.Forms.Label();
            this.btn_explorer2 = new System.Windows.Forms.Button();
            this.textSaveDstPath = new System.Windows.Forms.TextBox();
            this.tabControl1 = new System.Windows.Forms.TabControl();
            this.tabPage1 = new System.Windows.Forms.TabPage();
            this.tabPage2 = new System.Windows.Forms.TabPage();
            this.label1 = new System.Windows.Forms.Label();
            this.btn_explorer1 = new System.Windows.Forms.Button();
            this.textTargetPath = new System.Windows.Forms.TextBox();
            this.tabControl1.SuspendLayout();
            this.tabPage1.SuspendLayout();
            this.SuspendLayout();
            // 
            // listView
            // 
            this.listView.Font = new System.Drawing.Font("Meiryo UI", 9F);
            this.listView.HideSelection = false;
            this.listView.Location = new System.Drawing.Point(6, 36);
            this.listView.Name = "listView";
            this.listView.Size = new System.Drawing.Size(390, 200);
            this.listView.TabIndex = 0;
            this.listView.TabStop = false;
            this.listView.UseCompatibleStateImageBehavior = false;
            // 
            // label2
            // 
            this.label2.Font = new System.Drawing.Font("Meiryo UI", 9F, System.Drawing.FontStyle.Bold);
            this.label2.ForeColor = System.Drawing.SystemColors.ControlText;
            this.label2.Location = new System.Drawing.Point(6, 10);
            this.label2.Margin = new System.Windows.Forms.Padding(3);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(133, 20);
            this.label2.TabIndex = 5;
            this.label2.Text = "Download Contents";
            // 
            // btn_download
            // 
            this.btn_download.Font = new System.Drawing.Font("Meiryo UI", 9F);
            this.btn_download.Location = new System.Drawing.Point(316, 256);
            this.btn_download.Name = "btn_download";
            this.btn_download.Size = new System.Drawing.Size(80, 23);
            this.btn_download.TabIndex = 0;
            this.btn_download.TabStop = false;
            this.btn_download.Text = "Download";
            this.btn_download.Click += new System.EventHandler(this.btn_download_Click);
            // 
            // label4
            // 
            this.label4.Font = new System.Drawing.Font("Meiryo UI", 9F, System.Drawing.FontStyle.Bold);
            this.label4.Location = new System.Drawing.Point(6, 260);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(148, 20);
            this.label4.TabIndex = 10;
            this.label4.Text = "Save Destination Path";
            // 
            // btn_explorer2
            // 
            this.btn_explorer2.Font = new System.Drawing.Font("Meiryo UI", 9F);
            this.btn_explorer2.Location = new System.Drawing.Point(230, 256);
            this.btn_explorer2.Name = "btn_explorer2";
            this.btn_explorer2.Size = new System.Drawing.Size(80, 23);
            this.btn_explorer2.TabIndex = 8;
            this.btn_explorer2.TabStop = false;
            this.btn_explorer2.Tag = "Save";
            this.btn_explorer2.Text = "Explorer";
            this.btn_explorer2.UseVisualStyleBackColor = true;
            this.btn_explorer2.Click += new System.EventHandler(this.btn_explorer_Click);
            // 
            // textSaveDstPath
            // 
            this.textSaveDstPath.AllowDrop = true;
            this.textSaveDstPath.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.textSaveDstPath.Font = new System.Drawing.Font("Meiryo UI", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(128)));
            this.textSaveDstPath.Location = new System.Drawing.Point(6, 286);
            this.textSaveDstPath.Multiline = true;
            this.textSaveDstPath.Name = "textSaveDstPath";
            this.textSaveDstPath.Size = new System.Drawing.Size(390, 40);
            this.textSaveDstPath.TabIndex = 9;
            this.textSaveDstPath.TabStop = false;
            this.textSaveDstPath.Tag = "Save";
            // 
            // tabControl1
            // 
            this.tabControl1.Controls.Add(this.tabPage1);
            this.tabControl1.Controls.Add(this.tabPage2);
            this.tabControl1.Font = new System.Drawing.Font("Meiryo UI", 9F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(128)));
            this.tabControl1.Location = new System.Drawing.Point(12, 88);
            this.tabControl1.Name = "tabControl1";
            this.tabControl1.SelectedIndex = 0;
            this.tabControl1.Size = new System.Drawing.Size(414, 360);
            this.tabControl1.TabIndex = 12;
            // 
            // tabPage1
            // 
            this.tabPage1.Controls.Add(this.btn_download);
            this.tabPage1.Controls.Add(this.label4);
            this.tabPage1.Controls.Add(this.label2);
            this.tabPage1.Controls.Add(this.btn_explorer2);
            this.tabPage1.Controls.Add(this.listView);
            this.tabPage1.Controls.Add(this.textSaveDstPath);
            this.tabPage1.Location = new System.Drawing.Point(4, 24);
            this.tabPage1.Name = "tabPage1";
            this.tabPage1.Padding = new System.Windows.Forms.Padding(3);
            this.tabPage1.Size = new System.Drawing.Size(406, 332);
            this.tabPage1.TabIndex = 0;
            this.tabPage1.Text = "Download";
            this.tabPage1.UseVisualStyleBackColor = true;
            // 
            // tabPage2
            // 
            this.tabPage2.Location = new System.Drawing.Point(4, 24);
            this.tabPage2.Name = "tabPage2";
            this.tabPage2.Padding = new System.Windows.Forms.Padding(3);
            this.tabPage2.Size = new System.Drawing.Size(406, 332);
            this.tabPage2.TabIndex = 1;
            this.tabPage2.Text = "Upload";
            this.tabPage2.UseVisualStyleBackColor = true;
            // 
            // label1
            // 
            this.label1.Font = new System.Drawing.Font("Meiryo UI", 9F, System.Drawing.FontStyle.Bold);
            this.label1.Location = new System.Drawing.Point(13, 7);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(82, 20);
            this.label1.TabIndex = 15;
            this.label1.Text = "Target Path";
            // 
            // btn_explorer1
            // 
            this.btn_explorer1.Location = new System.Drawing.Point(332, 4);
            this.btn_explorer1.Name = "btn_explorer1";
            this.btn_explorer1.Size = new System.Drawing.Size(80, 23);
            this.btn_explorer1.TabIndex = 13;
            this.btn_explorer1.TabStop = false;
            this.btn_explorer1.Tag = "Target";
            this.btn_explorer1.Text = "Explorer";
            this.btn_explorer1.UseVisualStyleBackColor = true;
            this.btn_explorer1.Click += new System.EventHandler(this.btn_explorer_Click);
            // 
            // textTargetPath
            // 
            this.textTargetPath.AllowDrop = true;
            this.textTargetPath.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.textTargetPath.Location = new System.Drawing.Point(16, 31);
            this.textTargetPath.Multiline = true;
            this.textTargetPath.Name = "textTargetPath";
            this.textTargetPath.Size = new System.Drawing.Size(396, 40);
            this.textTargetPath.TabIndex = 14;
            this.textTargetPath.TabStop = false;
            this.textTargetPath.Tag = "Target";
            // 
            // UDDualTransfer
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(434, 456);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.btn_explorer1);
            this.Controls.Add(this.textTargetPath);
            this.Controls.Add(this.tabControl1);
            this.Font = new System.Drawing.Font("Meiryo UI", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(128)));
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Margin = new System.Windows.Forms.Padding(4);
            this.MaximizeBox = false;
            this.Name = "UDDualTransfer";
            this.Text = "UDDualTransfer";
            this.tabControl1.ResumeLayout(false);
            this.tabPage1.ResumeLayout(false);
            this.tabPage1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.ListView listView;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Button btn_download;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Button btn_explorer2;
        private System.Windows.Forms.TextBox textSaveDstPath;
        private System.Windows.Forms.TabControl tabControl1;
        private System.Windows.Forms.TabPage tabPage1;
        private System.Windows.Forms.TabPage tabPage2;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button btn_explorer1;
        private System.Windows.Forms.TextBox textTargetPath;
    }
}

