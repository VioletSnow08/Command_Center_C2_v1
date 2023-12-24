FROM mcr.microsoft.com/dotnet/runtime:7.0 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/sdk:7.0 AS build
WORKDIR /src
COPY ["c2_server/c2_server.csproj", "c2_server/"]
RUN dotnet restore "c2_server/c2_server.csproj"
COPY . .
WORKDIR "/src/c2_server"
RUN dotnet build "c2_server.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "c2_server.csproj" -c Release -o /app/publish /p:UseAppHost=false

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "c2_server.dll"]
