using MvvmHelpers;
using System;
using System.Collections.Generic;
using System.Text;

namespace WebAppCSC4008.Models
{
    public class Alert : ObservableObject
    {
        //public long ID;
        //public string University;
        //public string Room;
        //public string Module;
        //public string Lecturer;
        //public int GroupSize;
        //public DateTime DateTime;
        //public TimeSpan Duration;

        private long id;
        public long ID
        {
            get => id;
            set => SetProperty(ref id, value);
        }

        private string university;
        public string University
        {
            get => university;
            set => SetProperty(ref university, value);
        }

        private string room;
        public string Room
        {
            get => room;
            set => SetProperty(ref room, value);
        }

        private string module;
        public string Module
        {
            get => module;
            set => SetProperty(ref module, value);
        }

        private string lecturer;
        public string Lecturer
        {
            get => lecturer;
            set => SetProperty(ref lecturer, value);
        }

        private int groupSize;
        public int GroupSize
        {
            get => groupSize;
            set => SetProperty(ref groupSize, value);
        }

        private string dateTime;
        public string DateTime
        {
            get => dateTime;
            set => SetProperty(ref dateTime, value);
        }

        private double duration;
        public double Duration
        {
            get => duration;
            set => SetProperty(ref duration, value);
        }

        public string GetClass()
        {
            return "test";
        }

        public string GetModule()
        {
            return "test";
        }

        public string GetCourse()
        {
            return "test";
        }
    }
}
