import React from "react";
import { View, StyleSheet, StatusBar, Text, Button } from "react-native";
import BackGround from "./src/components/backgroud/index.js";
import LogoMaestri from "./src/components/iconMaestri/index.js";
import colors from "./design-System/global-styles.js";


const app = () => {
  return (
    <View style={styles.container}>
      <StatusBar translucent backgroundColor="transparent" />
      <BackGround />
      <View style={styles.contentBox}>
        <LogoMaestri />
        <Text style={styles.title}> Seja bem vindo a Maestri </Text>
        <Button
        title="login"
        style={styles.button}
        />
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    position: "relative",
  },

  contentBox: {
    flex: 1,
    width: "100%",
    height: "100%",
    display: "flex",
    position: "absolute",
    justifyContent: "center",
    alignItems: "center",
  },

  title: {
    fontSize: 20,
    color: colors.softWhite,
    marginBottom: 20,
  },

  button: {
    width: 500,
    height:60,
    borderRadius:40
  },
});

export default app;
