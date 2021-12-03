using MvvmHelpers;
using System.Collections.Generic;

namespace WebAppCSC4008.Models
{
    public class GraphObject : ObservableObject
    {
        public string GraphText {  get; set; }
        public GraphObject(string graphtext)
        {
            this.GraphText = graphtext;
        }

        public static List<string> graphs = new List<string>
        {
            "Most Frequent Breach Location", "Average Breach Duration Per Group", "Breaches Per Module"
        };
    }
}
