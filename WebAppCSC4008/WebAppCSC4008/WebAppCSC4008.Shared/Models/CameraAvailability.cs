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

        public CameraAvailability(long id, string name, string status)
        {
            this.ID = id;
            this.Name = name;
            this.Status = status;
        }

        public static List<CameraAvailability> cameras()
        {
            return new List<CameraAvailability>(new CameraAvailability[3]
            {
                new CameraAvailability(1, "Camera1", "Online"),
                new CameraAvailability(2, "Camera2", "Online"),
                new CameraAvailability(3, "Camera3", "Offline")
            });
        }
    }
}
