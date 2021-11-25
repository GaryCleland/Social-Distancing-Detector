using System;
using System.Collections.Generic;
using System.IO;
using System.Text;
using SQLite;

namespace WebAppCSC4008.Output
{
    public class CameraDatabase
    {
#if __WASM__ || NETFX_CORE || __IOS__
        static SQLiteConnection Database;

        public CameraDatabase(string video)
        {
            var DatabasePath = Path.Combine(Windows.Storage.ApplicationData.Current.LocalFolder.Path, "CameraStreams.db");
            Database = new SQLiteConnection(DatabasePath);
            var exists = File.Exists(DatabasePath);
            if (!exists)
            {
                Database.CreateTable<streams>();
            }
            var strm = new streams() { stream = video };
            Database.Insert(strm);
            Database.Commit();
            Database.Close();
        }
#endif
    }

    public class streams
    {
        [PrimaryKey]
        public string stream { get; set; }
    }
}
