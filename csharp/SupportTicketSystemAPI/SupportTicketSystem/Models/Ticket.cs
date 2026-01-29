namespace SupportTicketSystem.Models
{
    public class Ticket
    {
        public Guid Id { get; set; }
        public string Title { get; set; }
        public string Description { get; set; }
        public string Creater { get; set; }
        public string Answer { get; set; }
        public string Support { get; set; }
        public int Status { get; set; }
    }
}
