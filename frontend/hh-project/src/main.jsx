import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.jsx'
import './index.css'
import VacanciesList from './VacanciesList.jsx'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'
import AddVacancy from './AddVacancy.jsx'
import AddResume from './AddResume.jsx'
import ResumesList from './ResumesList.jsx'
import LoginPage from './LoginPage.jsx'

const router = createBrowserRouter([
  {
    path:'/',
    element:<App/>
  },
  {
    path:'/vacancies',
    element:<VacanciesList/>
  },
  {
    path:'/add-vacancy',
    element:<AddVacancy/>
  },
  {
    path:'/add-resume',
    element:<AddResume/>
  },
  {
    path:'/resumes',
    element:<ResumesList/>
  },
  {
    path:'/login',
    element:<LoginPage/>
  }
])

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <RouterProvider router={router} />
  </StrictMode>,
)
