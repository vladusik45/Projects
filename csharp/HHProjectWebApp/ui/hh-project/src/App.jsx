import { useEffect, useState } from 'react'
import Header from './components/Header'
import VacancyCard from './components/VacancyCard'
import { Button } from './components/ui/button'
import { Link } from 'react-router-dom'
import { isSignIn, setSignIn } from './LoginPage'

function App() {
  
  return (
    <div >
      <Header/>
      <div className='mx-auto pt-20 flex flex-col items-center'>
        <Link to={'/add-vacancy'}>
          <Button className="mb-10 text-lg">Добавить вакансию</Button>
        </Link>
        <Link to={'/add-resume'}>
          <Button className="text-lg">Добавить резюме</Button>
        </Link>
      </div>
    </div>
  )
}

export default App
