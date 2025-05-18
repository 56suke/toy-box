using System;
using System.IO;
using System.Runtime.InteropServices;
using System.Windows.Forms;
using System.Drawing;
using Microsoft.WindowsAPICodePack.Dialogs;

namespace Sample
{
    public partial class UDDualTransfer : Form
    {   
        // メンバ変数
        SettingsManager m_settingsManager;

        public UDDualTransfer()
        {
            InitializeComponent();

            // textBox初期設定
            textTargetPath.ReadOnly = true;
            textTargetPath.BackColor = SystemColors.Window;

            textSaveDstPath.ReadOnly = true;
            textSaveDstPath.BackColor = SystemColors.Window;

            // イベントハンドラを設定
            // DragEnter→DragDropの順でイベント発生
            textTargetPath.DragEnter += textBox_DragEnter;
            textTargetPath.DragDrop += textBox_DragDrop;

            textSaveDstPath.DragEnter += textBox_DragEnter;
            textSaveDstPath.DragDrop += textBox_DragDrop;

            // 設定ファイルのパスを指定（実行ファイルの場所に保存）
            string configPath = "settings.json";

            // SettingsManager を使って設定をロード
            m_settingsManager = new SettingsManager(configPath);

            // 設定情報を取得
            string targetPath = m_settingsManager.Settings.TargetPath;
            string savePath = m_settingsManager.Settings.SavePath;

            textTargetPath.Text = targetPath;
            textSaveDstPath.Text = savePath;

            SetupListView();
            LoadRootItems();

            // tabの初期設定
            tabControl1.DrawMode = TabDrawMode.OwnerDrawFixed;
            tabControl1.DrawItem += tabControl1_DrawItem;

        }

        private void tabControl1_DrawItem(object sender, DrawItemEventArgs e)
        {
            TabControl tabControl = sender as TabControl;
            TabPage tabPage = tabControl.TabPages[e.Index];
            Rectangle tabRect = tabControl.GetTabRect(e.Index);
            bool isSelected = (e.Index == tabControl.SelectedIndex);

            Color backColor;

            switch (e.Index)
            {
                case 0: // Download タブ
                    backColor = isSelected ? Color.DodgerBlue : Color.LightBlue;
                    break;
                case 1: // Upload タブ
                    backColor = isSelected ? Color.Orange : Color.Moccasin;
                    break;
                default:
                    backColor = isSelected ? SystemColors.ControlLight : SystemColors.Control;
                    break;
            }

            using (Brush brush = new SolidBrush(backColor))
            {
                e.Graphics.FillRectangle(brush, tabRect);
            }

            // テキストを描画（中央揃え）
            TextRenderer.DrawText(e.Graphics, tabPage.Text, tabControl.Font, tabRect, Color.Black,
                TextFormatFlags.HorizontalCenter | TextFormatFlags.VerticalCenter);
        }

        // DragEnterイベント：ドラッグされたデータがファイルまたはフォルダなら許可
        private void textBox_DragEnter(object sender, DragEventArgs e)
        {
            if (e.Data.GetDataPresent(DataFormats.FileDrop))
            {
                e.Effect = DragDropEffects.Copy; // コピーとして処理
            }
            else
            {
                e.Effect = DragDropEffects.None;
            }
        }

        // DragDropイベント：ファイルパスを取得してTextBoxに表示
        private void textBox_DragDrop(object sender, DragEventArgs e)
        {
            string[] files = (string[])e.Data.GetData(DataFormats.FileDrop);
            if (files.Length > 0)
            {
                // 最初のファイルのパスを表示
                string path = files[0];

                if (sender is System.Windows.Forms.TextBox tb && tb.Tag is string tagStr)
                {
                    if (Enum.TryParse<ToolKind>(tagStr, out var kind))
                    {
                        switch (kind)
                        {
                            case ToolKind.Target:
                                textTargetPath.Text = path;
                                m_settingsManager.Settings.TargetPath = path;
                                m_settingsManager.Save();  // 変更を保存

                                SetupListView();
                                LoadRootItems();
                                break;
                            case ToolKind.Save:
                                textSaveDstPath.Text = path;
                                m_settingsManager.Settings.SavePath = path;
                                m_settingsManager.Save();  // 変更を保存
                                break;
                            default:
                                break;
                        }
                    }
                }
            }
        }

        private void SetupListView()
        {
            // ListView の設定
            listView.View = View.Details;
            listView.Columns.Clear();                       // カラムの重複を防ぐ
            listView.Columns.Add("Contents", 350);          // 幅のピクセル数を設定
            listView.CheckBoxes = true;                     // チェックボックスを表示
            listView.FullRowSelect = true;                  // アイテムを選択するとその行全体が選択される
            listView.HeaderStyle = ColumnHeaderStyle.None;  // ヘッダー非表示

            // ImageList の作成
            ImageList imageList = new ImageList();
            imageList.ImageSize = new Size(16, 16); // アイコンサイズ設定

            // システムのアイコン読込
            string shell32Path = System.Environment.GetFolderPath(System.Environment.SpecialFolder.System) + @"\SHELL32.dll";
            imageList.Images.Add(ExtractIcon(shell32Path, 70)); // ファイルアイコン
            imageList.Images.Add(ExtractIcon(shell32Path, 3));  // フォルダアイコン

            // ListViewにImageListを設定
            listView.SmallImageList = imageList;
        }

        private void LoadRootItems()
        {
            string path = m_settingsManager.Settings.TargetPath;

            // ファイルの場合、親フォルダパスを取得
            if (File.Exists(path))
            {
                path = Path.GetDirectoryName(path);
            }

            if (Directory.Exists(path))
            {
                try
                {
                    listView.Items.Clear();

                    // フォルダ追加
                    foreach (var dir in Directory.GetDirectories(path))
                    {
                        var item = new ListViewItem(Path.GetFileName(dir))
                        {
                            Tag = dir,
                            ImageIndex = 1,  // フォルダのアイコンを設定
                            Checked = true
                        };
                        item.SubItems.Add("folder");
                        listView.Items.Add(item);
                    }

                    // ファイル追加
                    foreach (var file in Directory.GetFiles(path))
                    {
                        var item = new ListViewItem(Path.GetFileName(file))
                        {
                            Tag = file,
                            ImageIndex = 0,  // ファイルのアイコンを設定
                            Checked = true
                        };
                        item.SubItems.Add("file");
                        listView.Items.Add(item);
                    }
                }
                catch (Exception ex)
                {
                    MessageBox.Show("ERROR!!: " + ex.Message);
                }
            }
        }

        [DllImport("shell32.dll", CharSet = CharSet.Auto)]
        private static extern int ExtractIconEx(string lpszFile, int nIconIndex, IntPtr[] phiconLarge, IntPtr[] phiconSmall, int nIcons);

        private static Icon ExtractIcon(string path, int index)
        {
            IntPtr[] largeIcons = new IntPtr[1];
            IntPtr[] smallIcons = new IntPtr[1];

            // 指定したインデックスからアイコンを取得
            ExtractIconEx(path, index, largeIcons, smallIcons, 1);

            // SmallIconを返却
            if (smallIcons[0] != IntPtr.Zero)
            {
                Icon icon = Icon.FromHandle(smallIcons[0]);
                return icon;
            }
            return SystemIcons.Application; // 取得できなかった場合の代替
        }

        private void btn_explorer_Click(object sender, EventArgs e)
        {
            var dialog = new CommonOpenFileDialog();
            dialog.IsFolderPicker = true;           // フォルダ選択モード
            dialog.Multiselect = false;             // 複数選択禁止
            dialog.AllowPropertyEditing = false;    // ユーザーによる名前変更・作成などを禁止
            dialog.EnsurePathExists = true;         // 存在するパスしか選べない


            if (sender is System.Windows.Forms.Button btn && btn.Tag is string tagStr)
            {
                if (Enum.TryParse<ToolKind>(tagStr, out var kind))
                {
                    switch (kind)
                    {
                        case ToolKind.Target:
                            if (dialog.ShowDialog() == CommonFileDialogResult.Ok)
                            {
                                string folderPath = dialog.FileName;
                                textTargetPath.Text = folderPath;

                                m_settingsManager.Settings.TargetPath = folderPath;
                                m_settingsManager.Save();  // 変更を保存

                                SetupListView();
                                LoadRootItems();
                            }
                            break;
                        case ToolKind.Save:
                            if (dialog.ShowDialog() == CommonFileDialogResult.Ok)
                            {
                                string folderPath = dialog.FileName;
                                textSaveDstPath.Text = folderPath;

                                m_settingsManager.Settings.SavePath = folderPath;
                                m_settingsManager.Save();  // 変更を保存
                            }
                            break;
                        default:
                            break;
                    }
                }
            }
        }

        private void btn_download_Click(object sender, EventArgs e)
        {
            // 現在の時刻でディレクトリ生成
            string dateFolderName = DateTime.Now.ToString("yyyy-MMdd-HHmmss");
            string targetDirPath = "";

            try
            {
                targetDirPath = Path.Combine(textSaveDstPath.Text, dateFolderName);
                Directory.CreateDirectory(targetDirPath);
            }
            catch (Exception ex)
            {
                MessageBox.Show($"エラーが発生しました: {ex.Message}");
            }

            // ListViewにてチェックがついているファイルorディレクトリをコピー
            bool allSuccess = true;
            bool hasCheckedItem = false;
            foreach (ListViewItem item in listView.Items)
            {
                if (item.Checked)
                {
                    hasCheckedItem = true;
                    try
                    {
                        string itemPath = Path.Combine(textTargetPath.Text, item.Text);
                        string dest = Path.Combine(targetDirPath, Path.GetFileName(item.Text));

                        if (File.Exists(itemPath))
                        {
                            // ファイルの場合
                            File.Copy(itemPath, dest, overwrite: true);
                        }
                        else if (Directory.Exists(itemPath))
                        {
                            // ディレクトリの場合（再帰的にコピー）
                            CopyDirectory(itemPath, dest);
                        }
                        else
                        {
                            MessageBox.Show("指定されたパスが存在しません。");
                            allSuccess = false;
                        }
                    }
                    catch (Exception ex)
                    {
                        MessageBox.Show($"エラーが発生しました: {ex.Message}");
                        allSuccess = false;
                    }
                }
            }


            if (hasCheckedItem)
            {
                if (allSuccess)
                {
                    MessageBox.Show("Save処理が完了しました。");
                }
                else
                {
                    MessageBox.Show("一部のファイル/フォルダでエラーが発生しました。");
                }
            }
            else
            {
                MessageBox.Show("チェックされた項目がありません。");
            }

        }

        void CopyDirectory(string sourceDir, string destinationDir)
        {
            // コピー先ディレクトリを作成（存在してもOK）
            Directory.CreateDirectory(destinationDir);

            // ファイルをすべてコピー
            foreach (string filePath in Directory.GetFiles(sourceDir))
            {
                string fileName = Path.GetFileName(filePath);
                string destFilePath = Path.Combine(destinationDir, fileName);
                File.Copy(filePath, destFilePath, overwrite: true);
            }

            // サブディレクトリも再帰的にコピー
            foreach (string subDir in Directory.GetDirectories(sourceDir))
            {
                string subDirName = Path.GetFileName(subDir);
                string destSubDir = Path.Combine(destinationDir, subDirName);
                CopyDirectory(subDir, destSubDir);
            }
        }

    }
}
