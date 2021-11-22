using SQLite;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Text;
using System.Threading.Tasks;
using WebAppCSC4008.Models;

namespace WebAppCSC4008.Data
{
    public class AlertDatabase
    {
        static SQLiteConnection Database;

        public AlertDatabase()
        {
            string DatabasePath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData), "Alert.db");
            Assembly assembly = IntrospectionExtensions.GetTypeInfo(typeof(App)).Assembly;
            Stream embeddedDatabaseStream = assembly.GetManifestResourceStream("WebAppCSC4008.Alert.db"); // NameOfProgram.NameOfDB.DBExtension

            if (!File.Exists(DatabasePath))
            {
                FileStream fileStreamToWrite = File.Create(DatabasePath);
                embeddedDatabaseStream.Seek(0, SeekOrigin.Begin);
                embeddedDatabaseStream.CopyTo(fileStreamToWrite);
                fileStreamToWrite.Close();
            }

            Database = new SQLiteConnection(DatabasePath);
            Database.CreateTable<Alert>();
        }

        public List<Alert> GetAlerts()
        {
            return Database.Table<Alert>().ToList();
        }

        public SQLiteConnection GetDatabase()
        {
            return Database;
        }
    }
}
