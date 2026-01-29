using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.ComponentModel;
using System.Linq;
using System.Windows;
using System.Windows.Input;

namespace Sweeper
{
    public class MinesweeperViewModel : INotifyPropertyChanged
    {
        private DifficultyLevel selectedDifficultyLevel;
        private ObservableCollection<Cell> gameBoard;
        public MinesweeperViewModel()
        {
            DifficultyLevels = new List<DifficultyLevel>()
            {
                new DifficultyLevel {Name = "Новичок: 10 бомб", BoardSize = 9 },
                new DifficultyLevel {Name = "Мастер: 40 бомб", BoardSize = 16 },
                new DifficultyLevel {Name = "Эксперт: 90 бомб", BoardSize = 25 },
            };

            SelectedDifficultyLevel = DifficultyLevels[0];
            GenerateGameBoard();
        }
        public List<DifficultyLevel> DifficultyLevels { get; }
        public DifficultyLevel SelectedDifficultyLevel
        {
            get { return selectedDifficultyLevel; }
            set
            {
                if (selectedDifficultyLevel != value)
                {
                    selectedDifficultyLevel = value;
                    GenerateGameBoard();
                    OnPropertyChanged(nameof(SelectedDifficultyLevel));
                }
            }
        }
        public ObservableCollection<Cell> GameBoard
        {
            get { return gameBoard; }
            set
            {
                if (gameBoard != value)
                {
                    gameBoard = value;
                    OnPropertyChanged(nameof(GameBoard));
                }
            }
        }
        private void GenerateGameBoard()
        {
            int boardSize = SelectedDifficultyLevel.BoardSize;
            Cell[,] gameBoard = new Cell[boardSize, boardSize];
            int mineCount = 0;

            switch (SelectedDifficultyLevel.Name)
            {
                case "Новичок: 10 бомб":
                    mineCount = 10;
                    break;
                case "Мастер: 40 бомб":
                    mineCount = 40;
                    break;
                case "Эксперт: 90 бомб":
                    mineCount = 90;
                    break;
                default:
                    break;
            }
            Random random = new Random();
            int count = 0;
            for (int row = 0; row < boardSize; row++)
            {
                for (int col = 0; col < boardSize; col++)
                {
                    Cell cell = new Cell()
                    {
                        Row = row,
                        Column = col,
                        IsMine = false,
                        IsRevealed = false,
                        Value = 0,
                        DisplayValue = string.Empty
                    };
                    gameBoard[row, col] = cell;
                }
            }
            while (count < mineCount)
            {
                int randomRow = random.Next(0, boardSize);
                int randomCol = random.Next(0, boardSize);
                Cell cell = gameBoard[randomRow, randomCol];
                if (!cell.IsMine)
                {
                    cell.IsMine = true;
                    count++;
                }
            }
            ObservableCollection<Cell> gameBoardCollection = new ObservableCollection<Cell>();

            for (int row = 0; row < boardSize; row++)
            {
                for (int col = 0; col < boardSize; col++)
                {
                    Cell cell = gameBoard[row, col];
                    gameBoardCollection.Add(cell);
                }
            }
            GameBoard = gameBoardCollection;

            foreach (Cell cell in GameBoard)
            {
                cell.CellClickCommand = CellClickCommand;
            }
        }
        private ICommand restartCommand;
        public ICommand RestartCommand
        {
            get
            {
                if (restartCommand == null)
                {
                    restartCommand = new RelayCommand<object>(RestartGame, CanRestartGame);
                }
                return restartCommand;
            }
        }
        private bool CanRestartGame(object parameter)
        {
            return true;
        }
        private void RestartGame(object parameter)
        {
            GenerateGameBoard();
        }
        private ICommand cellClickCommand;
        public ICommand CellClickCommand
        {
            get
            {
                if (cellClickCommand == null)
                {
                    cellClickCommand = new RelayCommand<Cell>(HandleCellClick, CanHandleCellClick);
                }
                return cellClickCommand;
            }
        }
        private bool CanHandleCellClick(Cell cell)
        {
            return cell != null && !cell.IsRevealed;
        }
        public ICommand cellRightClickCommand;
        public ICommand CellRightClickCommand
        {
            get
            {
                if (cellRightClickCommand == null)
                {
                    cellRightClickCommand = new RelayCommand<Cell>(HandleCellRightClick);
                }
                return cellRightClickCommand;
            }
        }
        private void HandleCellRightClick(Cell cell)
        {
            if (cell != null && !cell.IsRevealed)
            {
                cell.IsFlagged = !cell.IsFlagged;
                cell.DisplayValue = cell.IsFlagged ? "🚩" : string.Empty;
                if (GameBoard.Where(c => c.IsMine).All(c => c.IsFlagged))
                {
                    ShowMine();
                    MessageBox.Show("Вы выиграли!");
                    GenerateGameBoard();
                }
            }
        }
        private void ShowMine()
        {
            foreach (var cell in GameBoard) 
            {
                if (cell.IsMine)
                {
                    cell.DisplayValue = "💣";
                }
            }
        }
        private void HandleCellClick(Cell cell)
        {
            if (!CanHandleCellClick(cell))
                return; 
            if (!cell.IsRevealed)
            {
                cell.IsRevealed = true;

                if (cell.IsMine)
                {
                    ShowMine();
                    MessageBox.Show("Вы проиграли!");
                    GenerateGameBoard();
                }
                else
                {
                    cell.DisplayValue = CalculateCellValue(cell);
                    OnPropertyChanged(nameof(GameBoard));
                    if (cell.Value == 0)
                    {
                        OpenAdjacentCells(cell);
                    }
                }
            }
        }
        private void OpenAdjacentCells(Cell cell)
        {
            int[] offsets = { -1, 0, 1 };

            foreach (int rowOffSet in offsets)
            {
                foreach (int colOffSet in offsets)
                {
                    if (rowOffSet == 0 && colOffSet == 0)
                        continue;
                    int neighborRow = cell.Row + rowOffSet;
                    int neighborCol = cell.Column + colOffSet;

                    if (neighborRow >= 0 && neighborRow < SelectedDifficultyLevel.BoardSize && neighborCol >= 0 && neighborCol < SelectedDifficultyLevel.BoardSize)
                    {
                        Cell neighborCell = GameBoard[neighborRow * SelectedDifficultyLevel.BoardSize + neighborCol];

                        if (!neighborCell.IsRevealed && !neighborCell.IsMine)
                        {
                            neighborCell.IsRevealed = true;
                            neighborCell.DisplayValue = CalculateCellValue(neighborCell);
                            OnPropertyChanged(nameof(GameBoard));
                            if (neighborCell.Value == 0)
                            {
                                OpenAdjacentCells(neighborCell);
                            }
                        }
                    }
                }
            }
        }
        private string CalculateCellValue(Cell cell)
        {
            int minesCount = 0;

            int[] offsets = { -1, 0, 1 };

            foreach (int rowOffSet in offsets)
            {
                foreach (int colOffSet in offsets)
                {
                    if (rowOffSet == 0 && colOffSet == 0)
                        continue;
                    int neighborRow = cell.Row + rowOffSet;
                    int neighborCol = cell.Column + colOffSet;

                    if (neighborRow >= 0 && neighborRow < SelectedDifficultyLevel.BoardSize && neighborCol >= 0 && neighborCol < SelectedDifficultyLevel.BoardSize)
                    {
                        Cell neighborCell = GameBoard[neighborRow * SelectedDifficultyLevel.BoardSize + neighborCol];
                        if (neighborCell.IsMine)
                        {
                            minesCount++;
                        }
                    }
                }
            }
            if (minesCount > 0)
            {
                cell.Value = minesCount;
                cell.DisplayValue = cell.Value.ToString();
                return minesCount.ToString();
            }
            return string.Empty;
        }
        public event PropertyChangedEventHandler PropertyChanged;
        protected virtual void OnPropertyChanged(string propertyName) 
        {
            PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(propertyName));
        }
    }
}
