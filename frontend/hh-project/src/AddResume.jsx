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

function AddResume() {

    const [employmentTypeValue, setEmploymentTypeValue] = useState()
    const navigate=useNavigate()

    const API_URL="https://localhost:7219/api/"

    async function addClick(e) {
        e.preventDefault()
        var resumeTitle=document.getElementById("ResumeTitle").value
        var salary=document.getElementById("Salary").value
        var age=document.getElementById("Age").value
        var workExperience=document.getElementById("WorkExperience").value
        var education=document.getElementById("Education").value
        var schedule= employmentTypeValue
        var city=document.getElementById("City").value
        var contacts=document.getElementById("Contacts").value
        const data = {
            ResumeTitle: resumeTitle,
            Salary: salary,
            Age: age,
            WorkExperience: workExperience,
            Education: education,
            Schedule: schedule,
            City: city,
            Contacts: contacts}
        console.log(data)

        const headers = new Headers()
        headers.set("Content-Type", "application/json")

        fetch(API_URL+"Resume/AddResume",{
            method:"POST",
            headers: headers,
            body: JSON.stringify(data),
          }).then((result)=>{
            alert("Резюме успешно создано.")
          })

    }


  return (
    <>
    {isSignIn?  
        <div>
            <Header/>
            <div>
                <form className='p-5 border rounded-xl m-5 grid space-y-2'>
                    <label className='text-base'>Желаемая профессия</label>
                    <Input id="ResumeTitle" placeholder='Профессия'></Input>
                    <label className='text-base'>Ожидаемая заработная плата</label>
                    <Input id="Salary" placeholder='Зарплата' type="number"></Input>
                    <label className='text-base'>Возраст</label>
                    <Input id="Age" placeholder='Возраст' type="number"></Input>
                    <label className='text-base'>Предыдущий опыт работы</label>
                    <Input id="WorkExperience" placeholder='Опыт работы'></Input>
                    <label className='text-base'>Образование</label>
                    <Input id="Education" placeholder='Образование'></Input>
                    <label className='text-base'>Желаемый график работы</label>
                    <Select onValueChange={setEmploymentTypeValue} id="EmploymentTypeFull">
                        <SelectTrigger className="w-full">
                            <SelectValue placeholder="График работы" />
                        </SelectTrigger>
                        <SelectContent id="Schedule">
                            <SelectItem value="Полная занятость">Полная занятость</SelectItem>
                            <SelectItem value="Частичная занятость">Частичная занятость</SelectItem>
                            <SelectItem value="Свободный график">Свободный график</SelectItem>
                            <SelectItem value="Стажировка">Стажировка</SelectItem>
                            <SelectItem value="Вахта">Вахта</SelectItem>
                        </SelectContent>
                    </Select>
                    <label className='text-base'>Город</label>
                    <Input id="City" placeholder='Город'></Input>
                    <label className='text-base'>Контакты для связи</label>
                    <Input id="Contacts" placeholder='Контакты'></Input>
                    <Button onClick={addClick}>Сохранить</Button>
                </form>
            </div>
        </div>
        : <div className='grid items-center mt-10'>
        <Label className="text-xl mb-5 ml-5 ">Создать резюме могут только авторизованные пользователи.</Label>
        <Link to={'/login'}>
            <Button className="ml-5 bg-[#9fb1a6] text-lg">Войти</Button>
        </Link>
    </div>
    }
</>
  )
}

export default AddResume
