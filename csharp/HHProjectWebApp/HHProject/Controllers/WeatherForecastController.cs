using Microsoft.AspNetCore.Mvc;
using System.Data;
using System.Data.SqlClient;

namespace HHProject.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class WeatherForecastController : ControllerBase
    {
        private static readonly string[] Summaries = new[]
        {
            "Freezing", "Bracing", "Chilly", "Cool", "Mild", "Warm", "Balmy", "Hot", "Sweltering", "Scorching"
        };

        private readonly ILogger<WeatherForecastController> _logger;

        public WeatherForecastController(ILogger<WeatherForecastController> logger)
        {
            _logger = logger;
        }

        [HttpGet(Name = "GetWeatherForecast")]
        public IEnumerable<WeatherForecast> Get()
        {
            return Enumerable.Range(1, 5).Select(index => new WeatherForecast
            {
                Date = DateOnly.FromDateTime(DateTime.Now.AddDays(index)),
                TemperatureC = Random.Shared.Next(-20, 55),
                Summary = Summaries[Random.Shared.Next(Summaries.Length)]
            })
            .ToArray();
        }
    }

    //namespace TestProject.Controllers
    //{
    //    [Route("api/[controller]")]
    //    [ApiController]
    //    public class ProjectController : ControllerBase
    //    {
    //        private IConfiguration _configuration;

    //        public ProjectController(IConfiguration configuration)
    //        {
    //            _configuration = configuration;
    //        }

    //        [HttpGet]
    //        [Route("GetNotes")]
    //        public JsonResult GetNotes()
    //        {
    //            string query = "select * from notes";
    //            DataTable dt = new DataTable();
    //            string sqlDatasource = _configuration.GetConnectionString("DB");
    //            SqlDataReader dataReader;
    //            using (SqlConnection myCon = new SqlConnection(sqlDatasource))
    //            {
    //                myCon.Open();
    //                using (SqlCommand cmd = new SqlCommand(query, myCon))
    //                {
    //                    dataReader = cmd.ExecuteReader();
    //                    dt.Load(dataReader);
    //                    dataReader.Close();
    //                    myCon.Close();
    //                }
    //            }

    //            return new JsonResult(dt);
    //        }

    //        [HttpPost]
    //        [Route("AddNotes")]
    //        public JsonResult AddNotes([FromForm] string newNotes)
    //        {
    //            string query = "insert into notes values(@newNotes)";
    //            DataTable dt = new DataTable();
    //            string sqlDatasource = _configuration.GetConnectionString("DB");
    //            SqlDataReader dataReader;
    //            using (SqlConnection myCon = new SqlConnection(sqlDatasource))
    //            {
    //                myCon.Open();
    //                using (SqlCommand cmd = new SqlCommand(query, myCon))
    //                {
    //                    cmd.Parameters.AddWithValue("@newNotes", newNotes);
    //                    dataReader = cmd.ExecuteReader();
    //                    dt.Load(dataReader);
    //                    dataReader.Close();
    //                    myCon.Close();
    //                }
    //            }

    //            return new JsonResult("Added successfully");
    //        }

    //        [HttpDelete]
    //        [Route("DeleteNotes")]
    //        public JsonResult DeleteNotes(int id)
    //        {
    //            string query = "delete from notes where id=@id";
    //            DataTable dt = new DataTable();
    //            string sqlDatasource = _configuration.GetConnectionString("DB");
    //            SqlDataReader dataReader;
    //            using (SqlConnection myCon = new SqlConnection(sqlDatasource))
    //            {
    //                myCon.Open();
    //                using (SqlCommand cmd = new SqlCommand(query, myCon))
    //                {
    //                    cmd.Parameters.AddWithValue("@id", id);
    //                    dataReader = cmd.ExecuteReader();
    //                    dt.Load(dataReader);
    //                    dataReader.Close();
    //                    myCon.Close();
    //                }
    //            }

    //            return new JsonResult("Deleted successfully");
    //        }
    //    }
    //}
}
