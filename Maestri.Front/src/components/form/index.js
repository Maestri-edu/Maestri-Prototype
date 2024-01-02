import { View } from "react-native"
import FieldSet from "../fieldSet"
import styles from "./styles"


const Form = ({fieldsSets,showFeedBack}) => {
    return (
        <View style={styles.form}>
            {fieldsSets.map(({label, placeholder, setState,isSecure,keyBoardtype,validationFn}) => <FieldSet
                key={label}
                label={label}
                placeholder={placeholder}
                setState={setState}
                showFeedBack={showFeedBack}
                isSecure={isSecure}
                keyBoardtype={keyBoardtype}
                validationFn={validationFn}
                />) 
            }
        </View>
    )
}

export default Form