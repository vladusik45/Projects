using HHProject.Models;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using System.Data.SqlClient;
using System.Data;

namespace HHProject.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class ResumeController : ControllerBase
    {
        private IConfiguration _configuration;

        public ResumeController(IConfiguration configuration)
        {
            _configuration = configuration;
        }
        [HttpGet]
        [Route("getResumes")]
        public JsonResult Get()
        {
            string query = "select * from resumes";
            DataTable dt = new DataTable();
            string sqlDatasource = _configuration.GetConnectionString("DB");
            SqlDataReader dataReader;
            using (SqlConnection myCon = new SqlConnection(sqlDatasource))
            {
                myCon.Open();
                using (SqlCommand cmd = new SqlCommand(query, myCon))
                {
                    dataReader = cmd.ExecuteReader();
                    dt.Load(dataReader);
                    dataReader.Close();
                    myCon.Close();
                }
            }
            return new JsonResult(dt);
        }

        [HttpPost]
        [Route("addResume")]
        public JsonResult Add(ResumeModel resume)
        {
            string query = "insert into resumes values(@resumeTitle, " +
                "@salary, @age, @workExperience, @education, @schedule, @city, @contacts)";
            DataTable dt = new DataTable();
            string sqlDatasource = _configuration.GetConnectionString("DB");
            SqlDataReader dataReader;
            using (SqlConnection myCon = new SqlConnection(sqlDatasource))
            {
                myCon.Open();
                using (SqlCommand cmd = new SqlCommand(query, myCon))
                {
                    cmd.Parameters.AddWithValue("@resumeTitle", resume.ResumeTitle);
                    cmd.Parameters.AddWithValue("@salary", resume.Salary);
                    cmd.Parameters.AddWithValue("@age", resume.Age);
                    cmd.Parameters.AddWithValue("@workExperience", resume.WorkExperience);
                    cmd.Parameters.AddWithValue("@education", resume.Education);
                    cmd.Parameters.AddWithValue("@schedule", resume.Schedule);
                    cmd.Parameters.AddWithValue("@city", resume.City);
                    cmd.Parameters.AddWithValue("@contacts", resume.Contacts);
                    dataReader = cmd.ExecuteReader();
                    dt.Load(dataReader);
                    dataReader.Close();
                    myCon.Close();
                }
            }
            return new JsonResult("Resume is added");
        }
        [HttpDelete]
        [Route("deleteResume")]
        public JsonResult Delete(int id)
        {
            string query = "delete from resumes where id=@id";
            DataTable dt = new DataTable();
            string sqlDatasource = _configuration.GetConnectionString("DB");
            SqlDataReader dataReader;
            using (SqlConnection myCon = new SqlConnection(sqlDatasource))
            {
                myCon.Open();
                using (SqlCommand cmd = new SqlCommand(query, myCon))
                {
                    cmd.Parameters.AddWithValue("@id", id);
                    dataReader = cmd.ExecuteReader();
                    dt.Load(dataReader);
                    dataReader.Close();
                    myCon.Close();
                }
            }
            return new JsonResult("Resume is deleted");
        }
    }
}
