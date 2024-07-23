# 앱 구성 관리하기

## Dotenv

`Config Service`는 패키지를 설치하면 자동으로 생성됨.

```bash
npm install @nestjs/config
```

`.env`파일에서 환경을 가져옴.

> .env파일은 Git에 커밋하면 안됨.


## Config에 Dotenv 적용

```typescript
// app.module.ts

import {ConfigModule, ConfigService} from '@nestjs/config'
...

const cookieSession = require('cookie-session');

@Module({
  imports: [
    ConfigModule.forRoot({
      isGlobal: true,
      envFilePath: `.env.${process.env.NODE_ENV}`,
    }),
    TypeOrmModule.forRootAsync({
      inject: [ConfigService],
      useFactory: (config: ConfigService) => {
        return {
          type: 'sqlite',
          database: config.get<string>('DB_NAME'),
          synchronize: true,
          entities: [User, Report],
        };
      },
    }),
    // TypeOrmModule.forRoot({
    //   type: 'sqlite',
    //   database: 'db.sqlite',
    //   entities: [User, Report],
    //   synchronize: true,
    // }),
    UsersModule,
    ReportsModule,
  ],
  controllers: [AppController],
  providers: [
    AppService,
    {
      provide: APP_PIPE,
      useValue: new ValidationPipe({
        whitelist: true,
      }),
    },
  ],
})
export class AppModule {
  configure(consumer: MiddlewareConsumer) {
    consumer
      .apply(
        cookieSession({
          keys: ['asdfasfd'],
        }),
      )
      .forRoutes('*');
  }
}
```

```bash
npm install cross-env
```

```json
  ...
  "start": "cross-env NODE_ENV=development nest start",
  "start:dev": "cross-env NODE_ENV=development nest start --watch",
  "start:debug": "cross-env NODE_ENV=development nest start --debug --watch --maxWorker=1",
  "start:prod": "node dist/main",
  ...
  "test": "cross-env NODE_ENV=test jest",
  ...
```

## Git에 env파일이 올라가지 않도록 설정하기

```bash
# .gitignore

.env.development
.env.test
...

```

> .gitignore에 추가하여 git에 올라가지 않도록 처리한다.