namespace Sweeper
{
    public class DifficultyLevel
    {
        public string Name { get; set; }
        public int BoardSize { get; set; }
        public override string ToString()
        {
            return Name;
        }
    }
}
