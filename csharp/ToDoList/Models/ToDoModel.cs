using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;

namespace Eghednevnik.Models
{
    class ToDoModel : INotifyPropertyChanged
    {
        public DateTime creationDate { get; set; } = DateTime.Now;

        private bool _isDone;

        public bool isDone1
        {
            get { return _isDone; }
            set
            {
                if (_isDone == value)
                    return;
                _isDone = value;
                OnPropertyChanged("isDone1");

            }
        }

        public event PropertyChangedEventHandler PropertyChanged;

        private string _text;
        public string text1
        {
            get { return _text; }
            set
            {
                if (_text == value)
                    return;
                _text = value;
                OnPropertyChanged("text1");
            }
        }

        protected virtual void OnPropertyChanged(string propertyName = "")
        {
            PropertyChanged?.Invoke(propertyName, new PropertyChangedEventArgs(propertyName));

        }
    }
}
