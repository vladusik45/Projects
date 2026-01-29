using Microsoft.AspNetCore.Authentication.JwtBearer;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;

namespace SupportTicketSystem.Controllers
{
    [ApiController]
    [Route("[controller]")]
    [Authorize(AuthenticationSchemes = JwtBearerDefaults.AuthenticationScheme)]
    public class AdminController(AdminService adminService) : Controller
    {
        [Authorize(Roles = "Admin")]
        [HttpPost("admin")]
        public IActionResult ChangeRole(string username, string role)
        {
            if (role == "Admin")
            {
                return BadRequest();
            }
            var user = adminService.ChangeRole(username, role);
            return Ok(user);
        }
    }
}
