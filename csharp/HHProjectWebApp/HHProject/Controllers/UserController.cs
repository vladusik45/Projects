using HHProject.Models;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using System.Data.SqlClient;
using System.Data;
using System.Reflection.PortableExecutable;

namespace HHProject.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class UserController : ControllerBase
    {
        private IConfiguration _configuration;

        public UserController(IConfiguration configuration)
        {
            _configuration = configuration;
        }

        [HttpPost]
        [Route("register")]
        public JsonResult Register(UserModel user)
        {
            string query = "insert into users values(@email, @password, 'user')";
            DataTable dt = new DataTable();
            string sqlDatasource = _configuration.GetConnectionString("DB");
            SqlDataReader dataReader;
            using (SqlConnection myCon = new SqlConnection(sqlDatasource))
            {
                myCon.Open();
                using (SqlCommand cmd = new SqlCommand(query, myCon))
                {
                    cmd.Parameters.AddWithValue("@email", user.Email);
                    cmd.Parameters.AddWithValue("@password", user.Password);
                    dataReader = cmd.ExecuteReader();
                    dt.Load(dataReader);
                    dataReader.Close();
                    myCon.Close();
                }
            }
            return new JsonResult("Success");
        }

        [HttpPost]
        [Route("login")]
        public IActionResult Login(UserModel user)
        {
            string query = "select * from users where email = @email and password = @password";
            DataTable dt = new DataTable();
            string sqlDatasource = _configuration.GetConnectionString("DB");
            SqlDataReader dataReader;
            bool isSignIn;
            using (SqlConnection myCon = new SqlConnection(sqlDatasource))
            {
                myCon.Open();
                using (SqlCommand cmd = new SqlCommand(query, myCon))
                {
                    cmd.Parameters.AddWithValue("@email", user.Email);
                    cmd.Parameters.AddWithValue("@password", user.Password);
                    dataReader = cmd.ExecuteReader();
                    try
                    {
                        if (dataReader.Read())
                        {
                            isSignIn = true;
                        }
                        else isSignIn = false;
                    }
                    finally
                    {
                        dataReader.Close();
                    }
                    myCon.Close();
                }
            }
            return isSignIn? Ok() : NotFound();
        }
    }
}
