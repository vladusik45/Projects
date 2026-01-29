import React from 'react'

function VacancyCard({vacancy, deleteVacancy}) {
  return (
    <div className='rounded-xl bg-white border hover:shadow-md m-2 p-4'>
      <p className='m-2 text-lg text-black float-right mr-4 cursor-pointer'
        onClick={()=>deleteVacancy(vacancy.Id)}>x</p>
      <h2 className='text-2xl'>{vacancy.VacancyTitle}</h2>
      <p>{new Intl.NumberFormat("ru-RU").format(vacancy.Salary)} ₽</p>
      <p>Опыт: {vacancy.WorkExperience}</p>
      <p>{vacancy.EmploymentType}</p>
      <p>{vacancy.City}</p>
      <p>Описание вакансии: {vacancy.Description}</p>
      <p>{vacancy.Contacts}</p>
    </div>
  )
}

export default VacancyCard
