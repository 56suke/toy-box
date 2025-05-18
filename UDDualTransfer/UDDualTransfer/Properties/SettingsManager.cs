using Newtonsoft.Json;
using System.IO;

namespace Sample
{    public class SettingsManager
    {
        private readonly string _filePath;
        public AppSettings Settings { get; private set; }

        public SettingsManager(string filePath)
        {
            _filePath = filePath;
            Load();
        }

        private void Load()
        {
            if (File.Exists(_filePath))
            {
                try
                {
                    string json = File.ReadAllText(_filePath);
                    Settings = JsonConvert.DeserializeObject<AppSettings>(json) ?? new AppSettings();
                }
                catch
                {
                    // JSONが壊れていたら初期値で
                    Settings = new AppSettings();
                }
            }
            else
            {
                // ファイルがなければ初期値で
                Settings = new AppSettings();
            }

            Save(); // ファイルがなければここで自動生成
        }

        public void Save()
        {
            var json = JsonConvert.SerializeObject(Settings, Formatting.Indented);
            File.WriteAllText(_filePath, json);
        }
    }
}
