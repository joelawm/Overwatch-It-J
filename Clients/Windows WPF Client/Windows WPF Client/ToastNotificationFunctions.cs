using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

//addd refrences for Toast
using Windows.Data.Xml.Dom;
using Windows.UI.Notifications;

namespace Windows_WPF_Client
{
    class ToastNotificationFunctions
    {
        private const String APP_ID = "Monitor";

        //notifications for ZFS
        public static void ZFSNotification(string NotificationType)
        {
            //title of the popup
            string title = "ZFS "+ NotificationType + " " + Settings.APP_NAME;
            //datatime of the popup
            string timeString = $"{DateTime.Now:HH:mm:ss}";
            string message = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa";
            //string thomasImage = "https://www.thomasclaudiushuber.com/thomas.jpg";

            string toastXmlString =
            $@"<toast><visual>
            <binding template='ToastGeneric'>
            <text>{title}</text>
            <text>{message}</text>
            </binding>
            </visual></toast>";

            //create the xml notifciation
            var xmlDoc = new XmlDocument();
            xmlDoc.LoadXml(toastXmlString);

            var toastNotification = new ToastNotification(xmlDoc);

            var toastNotifier = ToastNotificationManager.CreateToastNotifier();
            toastNotifier.Show(toastNotification);
        }
    }
}
