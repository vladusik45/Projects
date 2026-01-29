import React from 'react'
import { useEffect, useState } from 'react'
import Header from './components/Header'
import VacancyCard from './components/VacancyCard'
import { Button } from './components/ui/button'
import { Link } from 'react-router-dom'
import { isSignIn, setSignIn } from './LoginPage'
import { Label } from './components/ui/label'

function VacanciesList() {
  const [vacancies, setVacancies] = useState([])

  useEffect(()=>{
    getData()
  },[])

  async function getData() {
    const response = await fetch(API_URL + "Vacancy/getVacancies")
    const data = await response.json()
    console.log(data)
    console.log(isSignIn)
    setVacancies(data)
  }

  const API_URL="https://localhost:7219/api/"

  async function deleteVacancy(id) {
        
    console.log(id)
    fetch(API_URL+"Vacancy/deleteVacancy?id="+id,{
        method:"DELETE",
    }).then(res=>res.json())
    .then(()=>{
        getData()
    })
    }

  
  return (
    <div >
      <Header />
      <div className='flex items-center justify-between m-8 mb-5'>
        <Label className='text-3xl font-semibold'>Вакансии:</Label>
        {isSignIn?
            <Link to={'/add-vacancy'}>
                <Button className='bg-[#9fb1a6]'>Добавить вакансию</Button>
            </Link>
            :<Link to={'/login'}>
                <Button className='bg-[#9fb1a6]'>Войти</Button>
        </Link>
        }
      </div>
      <div>
        <div className='grid grid-cols-1 md:grid-cols-2 gap-3'>
          {vacancies?.map((vacancy, index)=>{ return (
            <div key={index}>
              <VacancyCard vacancy={vacancy} deleteVacancy={deleteVacancy}/>
            </div>
          )})}
        </div>
      </div>
    </div>
  )
}

export default VacanciesList
