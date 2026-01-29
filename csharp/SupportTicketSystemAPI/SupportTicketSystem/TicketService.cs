using SupportTicketSystem.Models;
using System.Data;

namespace SupportTicketSystem
{
    public class TicketService
    {
        private readonly ApplicationDbContext _context;

        public TicketService(ApplicationDbContext context)
        {
            _context = context;
        }
        public void CreateTicket(string title, string description, string creater)
        {
            var ticket = new Ticket()
            {
                Title = title,
                Description = description,
                Creater = creater,
                Answer = "",
                Support = "",
                Status = 0
            };
            _context.Tickets.Add(ticket);
            _context.SaveChanges();
        }
        public List<Ticket> GetOpenTickets()
        {
            return _context.Tickets
                .Where(t => t.Status == 0)
                .ToList();
        }
        public List<Ticket> GetClosedTickets()
        {
            return _context.Tickets
                .Where(t => t.Status == 1)
                .ToList();
        }
        public List<Ticket> GetAllTickets()
        {
            return _context.Tickets
                .ToList();
        }
        public List<Ticket> GetUserTickets(string username)
        {
            return _context.Tickets
                .Where (t => t.Creater == username)
                .ToList();
        }
        public Ticket CloseTicket(Guid id, string answer, string suppostName)
        {
            var ticket = _context.Tickets.FirstOrDefault(u => u.Id == id);
            if (ticket != null)
            {
                ticket.Answer = answer;
                ticket.Support = suppostName;
                ticket.Status = 1;
                _context.SaveChanges();
            }
            return ticket;
        }
    }
}
