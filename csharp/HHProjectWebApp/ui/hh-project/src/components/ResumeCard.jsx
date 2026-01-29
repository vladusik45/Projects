import React from 'react'
import { Label } from './ui/label'

function ResumeCard({resume, deleteResume}) {
    return (
        <div className='rounded-xl bg-white border hover:shadow-md m-2 p-4'>
          <p className='m-2 text-lg text-black float-right mr-4 cursor-pointer'
            onClick={()=>deleteResume(resume.Id)}>x</p>
          <Label className='text-2xl'>{resume.ResumeTitle}</Label>
          <p>{new Intl.NumberFormat("ru-RU").format(resume.Salary)} ₽</p>
          <p>Возраст: {resume.Age}</p>
          <p>Опыт работы: {resume.WorkExperience}</p>
          <p>Образование: {resume.Education}</p>
          <p>{resume.Schedule}</p>
          <p>{resume.City}</p>
          <p>{resume.Contacts}</p>
          
        </div>
      )
    }

export default ResumeCard
