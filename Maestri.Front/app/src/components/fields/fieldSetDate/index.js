import { useState } from "react"
import { View, Button,TextInput } from "react-native"
import DatePicker from 'react-native-date-picker'

const FieldSetDate = () => {

  const [date, setDate] = useState(new Date())
  const [open, setOpen] = useState(false)

  return (
    <View>
      <Button title="Open" onPress={() => setOpen(true)} />
      <TextInput keyboardType=""/>
    </View>
  )
}

export default FieldSetDate