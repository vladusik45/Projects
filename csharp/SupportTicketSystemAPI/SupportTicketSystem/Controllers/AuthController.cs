using Microsoft.AspNetCore.Mvc;
using SupportTicketSystem.Authorization;
using SupportTicketSystem.Models;

namespace SupportTicketSystem.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class AuthController(UserService userService) : Controller
    {
        [HttpPost("/register")]
        public IActionResult Register([FromBody]RegisterRequest registerRequest)
        {
            userService.Register(registerRequest.Username, registerRequest.Password, registerRequest.Role);
            return Ok($"Registration is succesfully, {registerRequest.Username}.");
        }

        [HttpPost("/login")]
        public IActionResult Login([FromBody] LoginRequest loginRequest)
        {
            var token = userService.Login(loginRequest.Username, loginRequest.Password);
            if (token != null)
            {
                HttpContext.Response.Cookies.Append("myToken", token);
                return Ok($"Login is succesfully, {loginRequest.Username}.");
            }
            return Unauthorized();
        }
    }
}
