using Api1.Models;
using Microsoft.AspNetCore.Mvc;

namespace Api1.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class AuthController(AccountService accountService) : Controller
    {
        [HttpPost("register")]
        public IActionResult Register([FromBody]User request)
        {
            accountService.Register(request.Name, request.Email, request.Password, request.DateOfBirth);
            return Ok();
        }

        [HttpPost("login")]
        public IActionResult Login([FromBody] LoginRequest loginRequest)
        {
            var token = accountService.Login(loginRequest.Username, loginRequest.Password);
            HttpContext.Response.Cookies.Append("myToken", token);
            return Ok(token);
        }
    }
}