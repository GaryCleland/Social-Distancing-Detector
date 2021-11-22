using MvvmHelpers;
using System;
using System.Collections.Generic;
using System.Text;

namespace WebAppCSC4008.Models
{
    public class CameraAvailability : ObservableObject
    {
        public long ID { get; set; }
        public string Name { get; set; }
        public string Status { get; set; }
        public string Room { get; set; }
        public string University { get; set; }

        public CameraAvailability(long id, string name, string status, string room, string university)
        {
            this.ID = id;
            this.Name = name;
            this.Status = status;
        }

        public static List<CameraAvailability> cameras()
        {
            return new List<CameraAvailability>(new CameraAvailability[3]
            {
                new CameraAvailability(1, "Camera1", "Online", "CSB 02/27", "Queen's University Belfast"),
                new CameraAvailability(2, "Camera2", "Online", "CSB 01/03", "Queen's University Belfast"),
                new CameraAvailability(3, "Camera3", "Offline", "DKB 0G/118", "Queen's University Belfast")
            });
        }
    }
}
