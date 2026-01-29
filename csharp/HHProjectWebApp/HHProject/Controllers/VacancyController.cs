using HHProject.Models;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Newtonsoft.Json;
using System.Data;
using System.Data.SqlClient;

namespace HHProject.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class VacancyController : ControllerBase
    {
        private IConfiguration _configuration;

        public VacancyController(IConfiguration configuration)
        {
            _configuration = configuration;
        }
        [HttpGet]
        [Route("getVacancies")]
        public JsonResult Get()
        {
            string query = "select * from vacancies";
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
        [Route("addVacancy")]
        public JsonResult Add(VacancyModel vacancy)
        {
            string query = "insert into vacancies values(@vacancyTitle, " +
                "@salary, @workExperience, @employmentType, @city, @description, @contacts)";
            DataTable dt = new DataTable();
            string sqlDatasource = _configuration.GetConnectionString("DB");
            SqlDataReader dataReader;
            using (SqlConnection myCon = new SqlConnection(sqlDatasource))
            {
                myCon.Open();
                using (SqlCommand cmd = new SqlCommand(query, myCon))
                {
                    cmd.Parameters.AddWithValue("@vacancyTitle", vacancy.VacancyTitle);
                    cmd.Parameters.AddWithValue("@salary", vacancy.Salary);
                    cmd.Parameters.AddWithValue("@workExperience", vacancy.WorkExperience);
                    cmd.Parameters.AddWithValue("@employmentType", vacancy.EmploymentType);
                    cmd.Parameters.AddWithValue("@city", vacancy.City);
                    cmd.Parameters.AddWithValue("@description", vacancy.Description);
                    cmd.Parameters.AddWithValue("@contacts", vacancy.Contacts);
                    dataReader = cmd.ExecuteReader();
                    dt.Load(dataReader);
                    dataReader.Close();
                    myCon.Close();
                }
            }
            return new JsonResult("Vacancy is added");
        }
        [HttpDelete]
        [Route("deleteVacancy")]
        public JsonResult Delete(int id)
        {
            string query = "delete from vacancies where id=@id";
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
            return new JsonResult("Vacancy is deleted");
        }
    }
}
