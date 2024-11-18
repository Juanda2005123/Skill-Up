@echo off
REM Script para ejecutar pruebas de Behave
echo Ejecutando pruebas de Behave...

REM Ejecutar las pruebas por separado
behave features/registerFreelancer.feature
behave features/registerClient.feature
behave features/login.feature
behave features/notificationRegister.feature
behave features/createProject.feature
behave features/notificationCreateProject.feature
behave features/updateProject.feature
behave features/updateProfileClient.feature
behave features/notificationUpdateProfileClient.feature
behave features/updateProfileFreelancarAndNotification.feature
behave features/browseProject.feature
behave features/createChat.feature
behave features/applyProjectAndNotification.feature
behave features/chatAndNotification.feature

echo Pruebas de Behave completadas.
pause
