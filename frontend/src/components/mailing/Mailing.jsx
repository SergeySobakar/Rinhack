import React, { useState } from 'react'
import "./Mailing.css"
import { useMutation } from '@tanstack/react-query'
import axios from 'axios'
export default function Mailing() {

    const re = /[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?/g
    const [val, setVal] = useState("")

    const handleSendMail = (e) => {
        e.preventDefault()
        const isValidMail = re.test(val)
        if(isValidMail){
            try {
                mutate(val)
            } catch (error) {
                alert("Ошибка")
            }
        }
        else{
            alert("Неправильная почта")
            setVal("")
        }
    }

    const {mutate, isPending} = useMutation({
        mutationFn: async () => {
          await axios.post("")  
        }
    })

    return (
        <div className="mailing__cover">
            <h2 className="mailing__title">Уведомление в случае обнаружения опасности</h2>
            <div className="mailing__contenct">
                <form className="mailing__form">
                    <input value={val} onChange={(e) => setVal(e.target.value)} type="text" placeholder="Ваша почта"/>
                    <button onClick={handleSendMail} disabled={val.trim() === ""} className="btn" type="submit">{isPending ? "Процесс.." : "Запомнить для этой сессии"}</button>
                </form>
            </div>
        </div>
  )
}
