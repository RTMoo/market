# Используем стабильную LTS-версию Node.js
FROM node:22-slim


# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем только package.json и yarn.lock (если есть)
COPY package.json ./

# Удаляем node_modules (на всякий случай) и ставим зависимости через yarn
RUN npm install

# Копируем остальной код
COPY . .

# Открываем порт (если необходимо)
EXPOSE 5173

# Запускаем dev-сервер
CMD ["npm", "run", "dev", "--", "--host"]
