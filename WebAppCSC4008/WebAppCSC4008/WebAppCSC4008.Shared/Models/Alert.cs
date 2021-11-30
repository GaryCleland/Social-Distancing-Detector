using MvvmHelpers;
using System;
using System.Collections.Generic;
using System.Text;

namespace WebAppCSC4008.Models
{
    public class Alert : ObservableObject
    {
        public int DisplayID { get; set; }
        public string Id { get; set; }
        public string Camera { get; set; }
        public int Group_size { get; set; }
        public int Fob_data { get; set; }
        public string Date_time { get; set; }
        public double Duration { get; set; }
        public string Room { get; set; }
        public string Module { get; set; }
        public string University { get; set; }
        public string Lecturer { get; set; }
        private double _cfontsize = 14;
        public double CFontSize
        {
            get { return _cfontsize; }
            set { _cfontsize = value; }
        }
    }
}
