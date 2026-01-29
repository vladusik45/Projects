import React, { useEffect, useState } from 'react'
import Header from './components/Header'
import { Link } from 'react-router-dom'
import { Button } from './components/ui/button'
import ResumeCard from './components/ResumeCard'
import { isSignIn, setSignIn } from './LoginPage'

function ResumesList() {
    const [resumes, setResumes] = useState([])

    useEffect(()=>{
      getData()
    },[])
  
    async function getData() {
      const response = await fetch(API_URL + "Resume/getResumes")
      const data = await response.json()
      console.log(data)
      setResumes(data)
    }
  
    const API_URL="https://localhost:7219/api/"
  
    async function deleteResume(id) {
          
      console.log(id)
      fetch(API_URL+"Resume/deleteResume?id="+id,{
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
          <h2 className='text-3xl font-semibold'>Резюме:</h2>
          {isSignIn?
            <Link to={'/add-resume'}>
                <Button className='bg-[#9fb1a6]'>Добавить резюме</Button>
            </Link>
            :<Link to={'/login'}>
                <Button className='bg-[#9fb1a6]'>Войти</Button>
        </Link>
        }
        </div>
        <div>
          <div className='grid grid-cols-1 md:grid-cols-2 gap-3'>
            {resumes?.map((resume, index)=>{ return (
              <div key={index}>
                <ResumeCard resume={resume} deleteResume={deleteResume}/>
              </div>
            )})}
          </div>
        </div>
      </div>
    )
  }

export default ResumesList
