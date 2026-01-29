using Microsoft.AspNetCore.Authentication.JwtBearer;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using SupportTicketSystem.Models;
using System.IdentityModel.Tokens.Jwt;

namespace SupportTicketSystem.Controllers
{
    [ApiController]
    [Route("[controller]")]
    [Authorize(AuthenticationSchemes = JwtBearerDefaults.AuthenticationScheme)]
    public class TicketController(TicketService ticketService) : Controller
    {
        [HttpPost("client/create-ticket")]
        [Authorize(Roles ="Admin,Client")]
        public IActionResult CreateTicket(CreateTicketDto ticketDto)
        {
            var token = Request.Cookies["myToken"];

            if (string.IsNullOrEmpty(token))
            {
                return Unauthorized();
            }

            var handler = new JwtSecurityTokenHandler();
            var jwtToken = handler.ReadJwtToken(token);
            var username = jwtToken.Claims.FirstOrDefault(c => c.Type == "username")?.Value;

            if (string.IsNullOrEmpty(username))
            {
                return Unauthorized();
            }
            ticketService.CreateTicket(ticketDto.Title, ticketDto.Description, username);

            return Ok("Ticket is created.");
        }

        [HttpGet("support/get-open-tickets")]
        [Authorize(Roles ="Admin,Support")]
        public IActionResult GetOpenTickets() 
        {
            return Ok(ticketService.GetOpenTickets());
        }

        [HttpGet("support/get-closed-tickets")]
        [Authorize(Roles = "Admin,Support")]
        public IActionResult GetClosedTickets()
        {
            return Ok(ticketService.GetClosedTickets());
        }

        [HttpGet("support/get-all-tickets")]
        [Authorize(Roles = "Admin,Support")]
        public IActionResult GetAllTickets()
        {
            return Ok(ticketService.GetAllTickets());
        }

        [HttpGet("support/get-user-tickets")]
        [Authorize(Roles = "Admin,Support")]
        public IActionResult GetUserTickets(string username)
        {
            return Ok(ticketService.GetUserTickets(username));
        }

        [HttpGet("support/close-ticket")]
        [Authorize(Roles = "Admin,Support")]
        public IActionResult CloseTicket(Guid ticketId, string answer)
        {
            var token = Request.Cookies["myToken"];

            if (string.IsNullOrEmpty(token))
            {
                return Unauthorized(new { message = "Token not found in cookies." });
            }

            var handler = new JwtSecurityTokenHandler();
            var jwtToken = handler.ReadJwtToken(token);
            var supportName = jwtToken.Claims.FirstOrDefault(c => c.Type == "username")?.Value;

            if (string.IsNullOrEmpty(supportName))
            {
                return Unauthorized(new { message = "Username not found in token." });
            }
            return Ok(ticketService.CloseTicket(ticketId, answer, supportName));
        }
    }
}
