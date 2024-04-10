# TypeOrm

```typescript
//app.module.ts

...
@Module({
  imports: [TypeOrmModule.forRoot({
    type : 'sqlite',
    database : 'db.sqlite',
    entities : [User, Report],
    synchronize : true

  }), 
  UsersModule,
  ReportsModule
  ],
  ...

```

`synchronize` : 동기화 기능

synchronize를 true로 설정하면, TypeOrm이 모든 엔티티 구조를 살펴본 후 자동으로 데이터베이스 구조를 업데이트해줌.

`개발`환경에서만 사용해야 함. 운영환경에서 사용시, 열을 삭제하는 일이 생길 수 있음.
