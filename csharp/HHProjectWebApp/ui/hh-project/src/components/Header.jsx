import { isSignIn, setSignIn } from '@/LoginPage'
import React from 'react'
import { Link, useNavigate } from 'react-router-dom'

function Header() {

    const navigate = useNavigate()

    async function logOut() {
        setSignIn(false)
        navigate('/login')
    }
    
  return (
    <div className='flex justify-between items-center shadow-sm p-5 bg-[#e7f3f1]'>
        <img src='/example.png' width={150} height={100} />
        <ul className='hidden md:flex gap-16'>
            <Link to={'/vacancies'}>
                <li className='font-semibold hover:scale-105 transition-all cursor-pointer hover:text-primary'>Вакансии</li>
            </Link>
            <Link to={'/resumes'}>
                <li className='font-semibold hover:scale-105 transition-all cursor-pointer hover:text-primary'>Резюме</li>
            </Link>
            {isSignIn?<li className='hover:scale-105 transition-all cursor-pointer hover:text-primary' onClick={logOut}>Выйти</li>:<></>}
        </ul>
    </div>
  )
}

export default Header
