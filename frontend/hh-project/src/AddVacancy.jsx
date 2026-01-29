import React, { useState } from 'react'
import { Button } from './components/ui/button'
import {
    Select,
    SelectContent,
    SelectItem,
    SelectTrigger,
    SelectValue,
  } from "@/components/ui/select"
import { Input } from './components/ui/input'
import Header from './components/Header'
import { Link, useNavigate } from 'react-router-dom'
import { isSignIn, setSignIn } from './LoginPage'
import { Label } from './components/ui/label'

function AddVacancy() {

    const [employmentTypeValue, setEmploymentTypeValue] = useState()

    const API_URL="https://localhost:7219/api/"

    async function addClick(e) {
        e.preventDefault()

        var vacancyTitle=document.getElementById("VacancyTitle").value
        var salary=document.getElementById("Salary").value
        var workExperience=document.getElementById("WorkExperience").value
        var employmentType= employmentTypeValue
        var city=document.getElementById("City").value
        var description=document.getElementById("Description").value
        var contacts=document.getElementById("Contacts").value
        const data = {
            VacancyTitle: vacancyTitle,
            Salary: salary,
            WorkExperience: workExperience,
            EmploymentType: employmentType,
            City: city,
            Description: description,
            Contacts: contacts}
        console.log(data)

        const headers = new Headers()
        headers.set("Content-Type", "application/json")

        fetch(API_URL+"Vacancy/AddVacancy",{
            method:"POST",
            headers: headers,
            body: JSON.stringify(data),
          }).then((result)=>{
            console.log(result.status)
            alert("Вакансия успешно создана.")
          })

    }


  return (
    <>
    {isSignIn?
        <div>
            <Header/>
            <div>
                <form className='p-5 border rounded-xl m-5 grid space-y-2'>
                    <label className='text-base'>Название вакансии</label>
                    <Input id="VacancyTitle" placeholder='Название вакансии'></Input>
                    <label className='text-base'>Предлагаемая заработная плата</label>
                    <Input id="Salary" placeholder='Зарплата' type="number"></Input>
                    <label className='text-base'>Требуемый опыт работы</label>
                    <Input id="WorkExperience" placeholder='Опыт работы'></Input>
                    <label className='text-base'>Тип занятости</label>
                    <Select onValueChange={setEmploymentTypeValue} id="EmploymentTypeFull">
                        <SelectTrigger className="w-full">
                            <SelectValue placeholder="Тип занятости" />
                        </SelectTrigger>
                        <SelectContent id="EmploymentType">
                            <SelectItem value="Полная занятость">Полная занятость</SelectItem>
                            <SelectItem value="Частичная занятость">Частичная занятость</SelectItem>
                            <SelectItem value="Свободный график">Свободный график</SelectItem>
                            <SelectItem value="Стажировка">Стажировка</SelectItem>
                            <SelectItem value="Вахта">Вахта</SelectItem>
                        </SelectContent>
                    </Select>
                    <label className='text-base'>Город</label>
                    <Input id="City" placeholder='Город'></Input>
                    <label className='text-base'>Описание вакансии</label>
                    <Input id="Description" placeholder='Описание'></Input>
                    <label className='text-base'>Контакты для связи</label>
                    <Input id="Contacts" placeholder='Контакты'></Input>
                    <Button onClick={addClick}>Сохранить</Button>
                </form>
            </div>
        </div>
        : <div className='grid items-center mt-10'>
            <Label className="text-xl mb-5 ml-5 ">Создать вакансию могут только авторизованные пользователи.</Label>
            <Link to={'/login'}>
                <Button className="ml-5 bg-[#9fb1a6] text-lg">Войти</Button>
            </Link>
        </div>
    }
    </>
  )
}

export default AddVacancy
