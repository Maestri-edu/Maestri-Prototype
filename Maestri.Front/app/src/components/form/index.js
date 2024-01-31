import { View } from "react-native"
import FieldSet from "../fields/fieldSet"
import styles from "./styles"

const Form = ({fieldsSets,showFeedBack}) => {
    return (
        <View style={styles.form}>
            {fieldsSets.map(({Component = FieldSet,label,onEvent, placeholder, setState,isSecure,keyBoardtype,validationFn,data}) => <Component
                key={label}
                label={label}
                placeholder={placeholder}
                setState={setState}
                showFeedBack={showFeedBack}
                isSecure={isSecure}
                keyBoardtype={keyBoardtype}
                validationFn={validationFn}
                data={data}
                onEvent={onEvent}
                />) 
            }
        </View>
    )
}

export default Form