using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Security.Policy;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Input;

namespace Sweeper
{
        public class Cell : INotifyPropertyChanged
        {
            private bool isMine;
            private bool isRevealed;
            private int value;
            private string displayValue;
            private ICommand cellClickCommand;
            private int row;
            private int column;
            private bool isFlagged;
            public bool IsFlagged
            {
                get { return isFlagged; }
                set
                {
                    if(isFlagged!= value) 
                    {
                        isFlagged = value;
                        OnPropertyChanged(nameof(IsFlagged));
                    }
                }
            }
            public bool IsMine
            {
                get { return isMine; }
                set
                {
                    if (isMine != value)
                    {
                        isMine = value;
                        OnPropertyChanged(nameof(IsMine));
                    }
                }
            }
            public bool IsRevealed
            {
                get { return isRevealed; }
                set 
                {
                    if (isRevealed != value) 
                    {
                        isRevealed = value;
                        OnPropertyChanged(nameof(IsRevealed));
                    }
                }
            }
            public int Value
            {
                get { return value; }
                set
                {
                    if (this.value != value)
                    {
                        this.value = value;
                        OnPropertyChanged(nameof(Value));
                    }
                }
            }
            public string DisplayValue
            {
                get { return displayValue; }
                set
                {
                    if (displayValue != value)
                    {
                        displayValue = value;
                        OnPropertyChanged(nameof(DisplayValue));
                    }
                }
            }
            public ICommand CellClickCommand
            {
                get { return cellClickCommand; }
                set
                {
                    if (cellClickCommand != value)
                    {
                        cellClickCommand = value;
                        OnPropertyChanged(nameof(CellClickCommand));
                    }
                }
            }
            public int Row
            {
                get { return row; }
                set
                {
                    if (row != value)
                    {
                        row = value;
                        OnPropertyChanged(nameof(Row));
                    }
                }
            }
            public int Column
            {
                get { return column; }
                set
                {
                    if (column != value)
                    {
                        column = value;
                        OnPropertyChanged(nameof(Column));
                    }
                }
            }
            public event PropertyChangedEventHandler PropertyChanged;
            protected virtual void OnPropertyChanged(string propertyName)
            {
                PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(propertyName));
            }
        }
    }

