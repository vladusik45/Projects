import React from 'react'
import {
    Card,
    CardContent,
    CardDescription,
    CardFooter,
    CardHeader,
    CardTitle,
  } from "@/components/ui/card"
  import { Input } from "@/components/ui/input"
  import { Label } from "@/components/ui/label"
  import {
    Tabs,
    TabsContent,
    TabsList,
    TabsTrigger,
  } from "@/components/ui/tabs"
import { Button } from './ui/button'

function RegisterCard({registerClick}) {
  return (
    <div>
      <Card>
          <CardHeader>
            <CardTitle>Регистрация</CardTitle>
            <CardDescription>
              Регистрация необходима для возможности создания вакансий и резюме.
            </CardDescription>
          </CardHeader>
          <CardContent className="space-y-2">
            <div className="space-y-1">
              <Label htmlFor="current">Введите Email <span className='text-red-500'>*</span></Label>
              <Input id="newEmail" placeholder="Email"/>
            </div>
            <div className="space-y-1">
              <Label htmlFor="new">Придумайте пароль <span className='text-red-500'>*</span></Label>
              <Input id="newPassword" type="password" placeholder="Пароль" />
            </div>
          </CardContent>
          <CardFooter>
            <Button onClick={registerClick}>Зарегистрироваться</Button>
          </CardFooter>
        </Card>
    </div>
  )
}

export default RegisterCard
